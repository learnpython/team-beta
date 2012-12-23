# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserProfile(models.Model):
    TYPE_CHOICE = (
        ('regular', _(u'Регулярный пользователь')),
        ('agent', _(u'Контрагент')),
    )

    user = models.ForeignKey(User, verbose_name=_(u'Пользователь'), unique=True)

    user_type = models.CharField(_(u'Тип пользователя'), choices=TYPE_CHOICE,
        max_length=20)
    birthday = models.DateField(_(u'Дата рождения'), blank=True, null=True)
    city = models.CharField(_(u'Город'), help_text=_(u'Например: Киев'),
        max_length=25, blank=True)
    address = models.TextField(_('Адрес'),
        help_text=_(u'Например: ул. Ракетная 26, корпус 2, кв.20'), blank=True)
    phone = models.CharField(_(u'Телефон'),
        help_text=_(u'Например: (044) 524-18-03'), max_length=25, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.user, self.user_type)

    class Meta:
        verbose_name = _(u'Профиль')
        verbose_name_plural = _(u'Профили')
