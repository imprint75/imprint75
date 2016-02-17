from django.conf.urls import url

import experiments.views

urlpatterns = [
    url(r'^/?$', experiments.views.index, name='experiments.index'),
    url(r'^music_search/?$', experiments.views.music_search,
        name='experiements.music_search'),
]
