# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from zo.profile.forms import MyUserCreateForm
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == 'POST':
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            # email = form.clean()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                # email=email,
                                password=password)
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            return HttpResponseRedirect('/')
    else:
        form = MyUserCreateForm()
    return render(request, 'flatpages/default.html', {"form": form})
