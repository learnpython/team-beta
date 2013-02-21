# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from contragents.models import Category, Contragent
from profile.forms import MyUserCreateForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from calendar import HTMLCalendar, Calendar
from datetime import date, datetime, timedelta
from timeslots.models import TimeSlotDay


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
    if current.parent:
        parent_slug = current.parent.slug
    else:
        parent_slug = '/'
    categories = Category.objects.filter(parent_id=current.id)
    parents = current.get_parents()
    businesses = Contragent.objects.filter(main_category=current.id)

    return render(request, 'cat_and_cot.html', {"form": form,
                                            "categories": categories,
                                            "current": current,
                                            "parent_slug": parent_slug,
                                            "parents": parents[::-1],
                                            "businesses": businesses,
                                            }
                    )


def contragent(request, cat_name, contr_id):
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
        business = Contragent.objects.get(id=contr_id)
    except ObjectDoesNotExist:
        messages.error(request, 'Сведения о предприятии не найдены')
        return render(request, 'index.html')
    category = Category.objects.get(id=business.main_category_id)
    parents = category.get_parents()
    business.visits += 1
    business.save()
    return render(request, 'contragent.html',
                        {"b": business,
                        "current": category,
                        "parents": parents[::-1],
                        })
