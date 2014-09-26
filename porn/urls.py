from django.conf.urls import patterns, url

from porn import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^country/$', views.country, name='country'),
)