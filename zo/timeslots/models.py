# -*- coding: utf-8 -*-
from django.db import models
from contragents.models import Contragent
from profile.models import UserProfile
from datetime import datetime


class TimeSlotDay(models.Model):
    contragent = models.ForeignKey(Contragent, verbose_name=u'Контрагент')
    date = models.DateField(u"Дата")
    start_time = models.TimeField(u'Время начала работы')
    end_time = models.TimeField(u'Время конца работы')
    duration = models.IntegerField(u'Длительность сессии', default=30)
    capacity = models.IntegerField(u"Максимальное количество человек на сессию")
    aviability = models.BooleanField('Возможность записи на этот день', default=False)
    
    def __unicode__(self):
        return datetime.strftime(self.date, '%d.%m.%y')


class Timeslot(models.Model):
    day = models.ForeignKey(TimeSlotDay, verbose_name=u'Настрйки на день')
    time = models.TimeField(u"Время")
    capacity = models.IntegerField(u"Максимальное количество человек на сессию")

    class Meta:
        verbose_name = u'Таймслот'
        verbose_name_plural = u'Таймслоты'

    def __unicode__(self):
        return (self.day.date.strftime('%d.%m.%Y') + ' ' +
            self.time.strftime('%H:%M:%S') + u'. Длительность сессии: ' +
            str(self.day.duration) + u' минут. Максимальная емкость: ' + str(self.capacity))


class Appointment(models.Model):
    timeslot = models.ForeignKey(Timeslot, verbose_name=u'Таймслот')
    user = models.ForeignKey(UserProfile)

    class Meta:
        verbose_name = u'Назначенная встреча'
        verbose_name_plural = u'Назначенные встречи'

    def __unicode__(self):
        return (self.user.user.username + u' записан на ' +
            str(self.timeslot.date) + ' ' + str(self.timeslot.time) +
            u' в ' + self.timeslot.contragent.name)
