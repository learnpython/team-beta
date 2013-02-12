from django.conf.urls import patterns, url
from contragents.views import show_category, contragent

urlpatterns = patterns('',
    url(r'^categories/(?P<cat_name>(\w|-)*$)', show_category, name='show_category'),
    url(r'^categories/(?P<cat_name>(\w|-)*)/(?P<contr_id>\d{1,5}$)', contragent, name='show_contragent'),
)
