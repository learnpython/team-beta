# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages


def reg(request):
    return render(request, 'register.html')


# def feed(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Спасибо за отзыв! Ваш отзыв скоро будет добавлен.')
#             return HttpResponseRedirect(reverse('feed'))
#     else:
#         form = FeedbackForm()

#     feeds = Feedback.objects.filter(is_active=True).order_by('-timestamp')
#     return render(request, 'feed.html',
#         {'feeds': feeds, 'form': form, 'current_page': 'feed'})
