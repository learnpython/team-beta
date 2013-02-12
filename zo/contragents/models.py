# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='родительская категория')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'

    def get_parents(self):
        if self.parent:
            current = self
            parents = []
            while current.parent is not None:
                parents.append(current.parent)
                current = current.parent
            return parents
        return []

    def __unicode__(self):
        if self.parent:
            return ' -> '.join([par.name for par in self.get_parents()[::-1]] + [self.name])
        return self.name


class Contragent(models.Model):
    # Здесь перечисляем уникальные поля которые Контр заполняет руками
    main_category = models.ForeignKey('Category', verbose_name='Основна категория')
    additional_categories = models.ManyToManyField('Category', blank=True, null=True,
        verbose_name=u'Дополнительные категории', related_name='additional_contragents')
    contr_name = models.CharField('Название', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    detail = models.TextField('Описание')
    region = models.ForeignKey('CityRegion')
    city = models.ForeignKey('City')
    street1 = models.CharField('Улица 1', max_length=100, blank=False)
    street2 = models.CharField('Улица 2', max_length=100, blank=True)
    building = models.CharField('Номер дома', max_length=3, blank=True)
    zipcode = models.CharField('Индекс', max_length=5, blank=True)
    longitude = models.FloatField('Долгота', max_length=10, blank=True, null=True)
    latitude = models.FloatField('Широта', max_length=10, blank=True, null=True)
    visits = models.PositiveIntegerField('Посещения', default=0)

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