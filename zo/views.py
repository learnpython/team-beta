# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from profile.forms import MyUserCreateForm, MyUserForm, MyUserProfileForm
from profile.models import Category, Contragent
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

@login_required
def profile(request):
    user = request.user
    user_profile = user.get_profile()
    contr = user_profile.user_contr
    return render(request, 'profile.html',
            {"user": user, "user_profile": user_profile, "contr": contr})


@login_required
def profile_edit(request):
    user = request.user
    user_profile = user.get_profile()

    if request.method == 'POST':
        form = MyUserForm(request.POST, instance=user)
        profile_form = MyUserProfileForm(request.POST, instance=user_profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'Вы успешно обновили профиль')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = MyUserForm(instance=user)
        profile_form = MyUserProfileForm(instance=user_profile)

    return render(request, 'profile_edit.html',
            {'form': form, 'profile_form': profile_form, "user": user, "user_profile": user_profile})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в ситему')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Неправильный логин или пароль')
            return HttpResponseRedirect(reverse('index'))


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
            return HttpResponseRedirect(reverse('profile_edit'))
    else:
        form = MyUserCreateForm()
    categories = Category.objects.filter(parent_id=None)
    return render(request, 'index.html', {"form": form, "categories": categories})


def show_category(request, cat_name):
    if request.method == 'POST':
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            return HttpResponseRedirect(reverse('profile_edit'))
    else:
        form = MyUserCreateForm()
    try:
        current = Category.objects.get(slug=cat_name)
    except ObjectDoesNotExist:
        messages.error(request, 'Категория не найдена')
        return render(request, 'index.html')
    try:
        parent = Category.objects.get(id=current.parent_id)
        parent_slug = parent.slug
    except ObjectDoesNotExist:
        parent_slug = '/'
    categories = Category.objects.filter(parent_id=current.id)
    parents = current.get_parents(current)
    businesses = Contragent.objects.filter(main_category=current.id)

    return render(request, 'cat_and_cot.html', {"form": form,
                                            "categories": categories,
                                            "current": current,
                                            "parent_slug": parent_slug,
                                            "parents": sorted(parents.iteritems(), reverse=True),
                                            "businesses": businesses,
                                            }
                    )
