from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import home.views
import work.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', home.views.index),
    url(r'^home/?', include('home.urls')),
    url(r'^work/?', include('work.urls')),
    url(r'^experiments/?', include('experiments.urls')),
    url(r'^info/?', work.views.index, name='work.index'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
