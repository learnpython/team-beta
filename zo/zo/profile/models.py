# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_mobile = models.CharField('Мобильный телефон', max_length=20)
    user_type = models.CharField('Тип пользователя', max_length=1)

    class Meta:
        ordering = ['user']


class Contragent(models.Model):
    contr_name = models.CharField('Название', max_length=20)
    contr_adress = models.CharField('Адресс', max_length=20)
    contr_type = models.CharField('Тип', max_length=20)
    contr_phone = models.CharField('Телефон', max_length=20)
    contr_detail = models.TextField('Описание')

    def __unicode__(self):
        return '%s %s %s %s' % (self.contr_name, self.contr_adress, self.contr_type, self.contr_detail)

    class Meta:
        ordering = ['contr_name']
