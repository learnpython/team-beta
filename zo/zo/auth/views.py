# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages


def register(request):
    return render(request, 'register.html')
