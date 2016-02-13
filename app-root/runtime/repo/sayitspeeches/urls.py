from django.conf.urls import patterns, include, url
from django.contrib import admin

from sayitspeeches.views import Index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sayitspeeches.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^speeches/', include('sayitspeeches.urls', namespace='sayit', app_name='speeches')),
    url(r'^admin/', include(admin.site.urls)),
)



