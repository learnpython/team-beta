# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    # Мобильный телефон
    mobile = models.CharField('Мобильный телефон', max_length=20, blank=True)
    # Следующая срока нужна для того что бы связать юзера и контрагент, если 0 - юзер
    # если нет - поле заполняем ид имени контрагента. ТОгда просто делать выборку.
    user_contr = models.ForeignKey('Contragent', blank=True, null=True)

    class Meta:
        ordering = ['user']


class Category(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='родительская категория')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'

    def get_parents(self, instance):
        if instance.parent:
            current = instance
            parents = {}
            position = 0
            while current.parent is not None:
                parents[position] = current.parent
                current = current.parent
                position += 1
            return parents
        return {}

    def __unicode__(self):
        if self.parent:
            return self.parent.name + ' -> ' + self.name
        return self.name


class Contragent(models.Model):
    # Здесь перечисляем уникальные поля которые Контр заполняет руками
    main_category = models.ForeignKey('Category', related_name='Основна категория')
    additional_category1 = models.ForeignKey('Category', blank=True, null=True, related_name='Дополнительная категория')
    additional_category2 = models.ForeignKey('Category', blank=True, null=True, related_name='Дополнительная категория 2')
    contr_name = models.CharField('Название', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    detail = models.TextField('Описание')
    region = models.ForeignKey('CityRegion')
    city = models.ForeignKey('City')
    street1 = models.CharField('Улица 1', max_length=100, blank=False)
    street2 = models.CharField('Улица 2', max_length=100, blank=True)
    building = models.CharField('Номер дома', max_length=3, blank=True)
    zipcode = models.CharField('Индекс', max_length=5, blank=True)
    longitude = models.FloatField('Долгота', max_length=10, blank=True, default=30.0)
    latitude = models.FloatField('Широта', max_length=10, blank=True, default=50.0)

    def __unicode__(self):
        return self.contr_name

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


def user_post_save(created, instance, **kwags):
    if created:
        UserProfile(user=instance).save()
models.signals.post_save.connect(user_post_save, sender=User)
