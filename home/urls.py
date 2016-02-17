from django.conf.urls import url

import home.views

urlpatterns = [
    url(r'^/?$', home.views.index, name='home')
]
