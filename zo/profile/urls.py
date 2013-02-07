from django.conf.urls import patterns, url
from django.contrib.auth.views import logout


urlpatterns = patterns('profile.views',
    url(r'^registration/$', 'registration' ,name='registration'),
    url(r'^logout/$', logout, {"next_page": "/"}, name='logout'),
    url(r'^login/$', 'login_user', name='login'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^profile/edit/$', 'profile_edit', name='profile_edit'),
    )