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
    contr_adress = models.ForeignKey('Address')
    contr_type = models.CharField('Тип', max_length=20)
    contr_phone = models.CharField('Телефон', max_length=20)
    contr_detail = models.TextField('Описание')

    def __unicode__(self):
        return '%s %s %s %s' % (self.contr_name, self.contr_adress, self.contr_type, self.contr_detail)

    class Meta:
        ordering = ['contr_name']


class Address(models.Model):
    OBLASTI = (
        ('KRY', u'АР Крым'),
        ('VIN', u'Винницкая обл'),
        ('VOL', u'Волынска обл'),
        ('DNI', u'Днепропетровская обл'),
        ('DON', u'Донецкая обл'),
        ('ZHY', u'Житомирская обл'),
        ('ZAK', u'Закарпатская обл'),
        ('ZAP', u'Запорожская обл'),
        ('IVA', u'Ивано-Франковская обл'),
        ('KYI', u'Киев'),
        ('KYO', u'Киевская обл'),
        ('KIR', u'Кировоградская обл'),
        ('LUH', u'Луганская обл'),
        ('LVI', u'Львовская обл'),
        ('MYK', u'Николаевская обл'),
        ('ODE', u'Одесская обл'),
        ('POL', u'Полтавская обл'),
        ('ROV', u'Ровенская обл'),
        ('SEV', u'Севастополь'),
        ('SUM', u'Сумская обл'),
        ('TER', u'Тернопольская обл'),
        ('KHA', u'Харьковская обл'),
        ('KHE', u'Херсонская обл'),
        ('KHM', u'Хмельницкая обл'),
        ('CHE', u'Черкасская обл'),
        ('CHG', u'Черниговская обл'),
        ('CHR', u'Черновицкая обл'),
        )

    region = models.CharField('Область', max_length=20, choices=OBLASTI)
    city = models.CharField('Город', max_length=100, blank=False)
    street_line1 = models.CharField('Улица 1', max_length=100, blank=False)
    street_line2 = models.CharField('Улица 2', max_length=100, blank=True)
    building = models.CharField('Номер дома', max_length=30, blank=True)
    zipcode = models.CharField('Индекс', max_length=5, blank=True)
    longitude = models.FloatField('Долгота', max_length=10, blank=True, default=30.0)
    latitude = models.FloatField('Широта', max_length=10, blank=True, default=50.0)
