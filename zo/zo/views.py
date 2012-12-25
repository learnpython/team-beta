# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from zo.profile.forms import MyUserCreateForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            messages.success(request, 'Спасибо за отзыв! Ваш отзыв скоро будет добавлен.')
            return HttpResponseRedirect('/')
    else:
        form = MyUserCreateForm()
    return render(request, 'register.html', {"form": form})
