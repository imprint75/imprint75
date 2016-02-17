from django.conf.urls import url

import work.views

urlpatterns = [
    url(r'^/?$', work.views.index, name='home'),
]
