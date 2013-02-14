# -*- coding: utf-8 -*-
from django.contrib import admin
from contragents.models import Contragent, City, CityRegion, Category


class ContragentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'detail', 'region',
        'city', 'street1', 'street2', 'building',
        'zipcode',
        'longitude', 'latitude',
        'main_category',
        "show_additional_categories",
        )
    search_filter = ('name')
    search_fields = ['name', ]

    def show_additional_categories(self, obj):
        return ', '.join([cat.name for cat in obj.additional_categories.all()])

admin.site.register(Contragent, ContragentAdmin)
admin.site.register(City)
admin.site.register(CityRegion)
admin.site.register(Category)