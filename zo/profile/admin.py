# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profile.models import UserProfile, Contragent, City, CityCode, CityRegion, MobileCode


class ProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ]


class ContragentAdmin(admin.ModelAdmin):
    list_display = ('contr_name', 'contr_phone', 'contr_detail', 'contr_region',
        'contr_city', 'contr_city_code', 'contr_street', 'contr_building',
        'contr_zipcode', 'ngitude', 'latitude')
    search_filter = ('contr_name')
    search_fields = ['contr_name', ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Contragent, ContragentAdmin)
admin.site.register(City)
admin.site.register(CityCode)
admin.site.register(CityRegion)
admin.site.register(MobileCode)
