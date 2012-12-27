# -*- coding: utf-8 -*-
from django.contrib import admin
from models import UserProfile, Contragent


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_mobile', 'user_type')
    search_filter = ('user')
    search_fields = ['user', ]


class UserContragent(admin.ModelAdmin):
    list_display = ('contr_name', 'contr_adress', 'contr_type', 'contr_phone', 'contr_detail')
    search_filter = ('contr_name')
    search_fields = ['contr_name', ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Contragent, UserContragent)
