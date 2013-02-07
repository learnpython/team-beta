# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profile.models import UserProfile, Contragent, City, CityRegion, Category


class ProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ]


class ContragentAdmin(admin.ModelAdmin):
    list_display = ('contr_name', 'phone', 'detail', 'region',
        'city', 'street1', 'street2', 'building',
        'zipcode',
        'longitude', 'latitude',
        'main_category',
        "show_additional_categories",
        )
    search_filter = ('contr_name')
    search_fields = ['contr_name', ]

    def show_additional_categories(self, obj):
        return ', '.join([cat.name for cat in obj.additional_categories.all()])



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Contragent, ContragentAdmin)
admin.site.register(City)
admin.site.register(CityRegion)
admin.site.register(Category)
