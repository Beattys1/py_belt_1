
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^friend_show$', views.friend_show),
    url(r'^user/(?P<id>[0-9]+)', views.user),
    url(r'^delete/(?P<id>[0-9]+)', views.delete),
    url(r'^add_friend/(?P<id>[0-9]+)', views.add_friend),

]
