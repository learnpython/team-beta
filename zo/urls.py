from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.contrib.auth.views import logout
from views import index, login_user, profile, profile_edit, show_category, contragent


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^logout/$', logout, {"next_page": "/"}, name='logout'),
    url(r'^login/$', login_user, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit/$', profile_edit, name='profile_edit'),
    url(r'^(?P<cat_name>(\w|-)*$)', show_category, name='show_category'),
    url(r'^(?P<cat_name>(\w|-)*)/(?P<contr_id>\d{1,5}$)', contragent, name='show_contragent'),
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
