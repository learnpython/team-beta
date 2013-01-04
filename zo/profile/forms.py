# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreateForm(UserCreationForm):
    # email = forms.EmailField(label="Email")
    # fullname = forms.CharField(label="Имя, Фамилия")

    class Meta:
        model = User
        fields = ("username",
                # "fullname",
                "email",
                "password1",
                "password2",
                )
