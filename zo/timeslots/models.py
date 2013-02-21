# -*- coding: utf-8 -*-
from django.db import models
from contragents.models import Contragent
from profile.models import UserProfile


class TimeSlotSettings(models.Model):
    weekdays = None
    start_time = models.TimeField()
    end_time = models.TimeField()


class Timeslot(models.Model):
    contragent = models.ForeignKey(Contragent, verbose_name=u'Контрагент')
    date = models.DateField(u"Дата")
    time = models.TimeField(u"Время")
    duration = models.IntegerField(u"Длительность сессии")
    capacity = models.IntegerField(u"Максимальное количество человек на сессию")

    class Meta:
        verbose_name = u'Таймслот'
        verbose_name_plural = u'Таймслоты'

    def __unicode__(self):
        return (self.date.strftime('%d.%m.%Y') + ' ' +
            self.time.strftime('%H:%M:%S') + u'. Длительность сессии: ' +
            str(self.duration) + u' минут. Максимальная емкость: ' + str(self.capacity))


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
