from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'earthporn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^porn/', include('porn.urls', namespace='porn')),
    url(r'^admin/', include(admin.site.urls)),
)
