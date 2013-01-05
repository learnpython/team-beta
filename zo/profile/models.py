# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    # Мобильный телефон
    mobile = models.CharField('Мобильный телефон', max_length=20)
    mobile_code = models.ForeignKey('MobileCode')
    # Следующая срока нужна для того что бы связать юзера и контрагент, если 0 - юзер
    # если нет - поле заполняем ид имени контрагента. ТОгда просто делать выборку.
    user_contr = models.CharField(max_length=4, default=0)

    class Meta:
        ordering = ['user']


class Contragent(models.Model):
    # Здесь перечисляем уникальные поля которые Контр заполняет руками
    contr_name = models.CharField('Название', max_length=20)
    contr_phone = models.CharField('Телефон', max_length=20)
    contr_detail = models.TextField('Описание')
    contr_region = models.ForeignKey('CityRegion')
    contr_city = models.ForeignKey('City')
    contr_city_code = models.ForeignKey('CityCode')
    contr_street = models.CharField('Улица 1', max_length=100, blank=False)
    contr_building = models.CharField('Номер дома', max_length=3, blank=True)
    contr_zipcode = models.CharField('Индекс', max_length=5, blank=True)
    ngitude = models.FloatField('Долгота', max_length=10, blank=True, default=30.0)
    latitude = models.FloatField('Широта', max_length=10, blank=True, default=50.0)

    def __unicode__(self):
        return '%s %s %s' % (self.contr_name, self.contr_detail, self.contr_street)

    class Meta:
        ordering = ['contr_name']


# Создадим классы со статическими данными которые будут выбираться из списков
# и заполним наши таблицы в БД
class City(models.Model):
    city = models.CharField('Город', max_length=100, blank=False)

    def __unicode__(self):
        return self.city


class CityRegion(models.Model):
    region = models.CharField('Область', max_length=20)

    def __unicode__(self):
        return self.region


class CityCode(models.Model):
    city_code = models.CharField('Код города', max_length=5)

    def __unicode__(self):
        return self.city_code


class MobileCode(models.Model):
    mobile_code = models.CharField('Код оператора', max_length=3, blank=False)

    def __unicode__(self):
        return self.mobile_code
