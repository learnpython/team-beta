from django import template
from calendar import HTMLCalendar, Calendar
from datetime import date, datetime, timedelta
from timeslots.models import TimeSlotDay

register = template.Library()


class TScalendar(HTMLCalendar):
    
    def __init__(self, business, year=date.today().year, month=date.today().month):
        self.firstweekday = 0
        self.business = business
        self.year = year
        self.month = month
        self.available_days_list = []
        
    def available_days(self):
        if not len(self.available_days_list):
            cal = Calendar()
            month_dates = cal.itermonthdates(self.year, self.month)
            for day in month_dates:
                timeslots = None
                if day > date.today():
                    timeslots = TimeSlotDay.objects.filter(date=day, aviability=True)
                if day == date.today():
                    timeslots = TimeSlotDay.objects.filter(date=day, end_time__gte=datetime.now() + timedelta(hours=1), aviability=True)
                if timeslots:
                    self.available_days_list.append(day.day)
        return self.available_days_list
    
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            body = ['<ul>']
            if date.today() == date(self.year, self.month, day):
                cssclass += ' calendar-today'
                body.append('<li>Сегодня</li>')
            if day in self.available_days():
                cssclass += ' calendar-available'
                body.append('<li>Есть свободное время</li>')
            body.append('</ul>')
            return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
        return self.day_cell('noday', '&nbsp;')
    
    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        return super(TScalendar, self).formatmonth(year, month, withyear)
    
    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
    
    
def do_calendar(parser, token):
    try:
        contragent, year, month = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
    return TScalendar(contragent, year, month)


register.tag("ts_calendar", do_calendar)
