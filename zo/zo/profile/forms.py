# -*- coding: utf-8 -*-

from django import forms
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

    # def save(self, commit=True):
    #     user = super(MyUserCreateForm, self).save(commit=False)
    #     # first_name, last_name = self.cleaned_data["fullname"].split()
    #     # user.first_name = first_name
    #     # user.last_name = last_name
    #     # user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
