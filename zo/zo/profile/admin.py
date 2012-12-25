# -*- coding: utf-8 -*-
from zo.profile import models
from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.UserProfile, UserProfileAdmin)
