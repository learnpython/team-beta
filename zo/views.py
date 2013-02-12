# -*- coding: utf-8 -*-
from profile.forms import MyUserCreateForm
from contragents.models import Category
from annoying.decorators import render_to


@render_to('index.html')
def index(request):
    form = MyUserCreateForm()
    categories = Category.objects.filter(parent_id=None)
    return {"form": form, "categories": categories}
