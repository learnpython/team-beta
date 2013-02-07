from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from views import index, show_category, contragent


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'', include('profile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^categories/(?P<cat_name>(\w|-)*$)', show_category, name='show_category'),
    url(r'^categories/(?P<cat_name>(\w|-)*)/(?P<contr_id>\d{1,5}$)', contragent, name='show_contragent'),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(
            r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ) + urlpatterns
