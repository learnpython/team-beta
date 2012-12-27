# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from profile.forms import MyUserCreateForm
from django.contrib.auth import authenticate, login


def profile(request):
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('profile.html', {'user': user})
    else:
        messages.error(request, 'Вы не вошли в систему')
        return HttpResponseRedirect('/')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в ситему')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Неправильный логин или пароль')
            return HttpResponseRedirect('/')


def index(request):
    if request.method == 'POST':
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            return HttpResponseRedirect('/')
    else:
        form = MyUserCreateForm()
    return render(request, 'flatpages/default.html', {"form": form})
