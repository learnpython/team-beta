# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    # Мобильный телефон
    mobile = models.CharField('Мобильный телефон', max_length=20, blank=True)
    # Следующая срока нужна для того что бы связать юзера и контрагент, если 0 - юзер
    # если нет - поле заполняем ид имени контрагента. ТОгда просто делать выборку.
    user_contr = models.ForeignKey('contragents.Contragent', blank=True, null=True)

    class Meta:
        ordering = ['user']

    def __unicode__(self):
        return self.user.username


def user_post_save(created, instance, **kwags):
    if created:
        UserProfile(user=instance).save()
models.signals.post_save.connect(user_post_save, sender=User)
