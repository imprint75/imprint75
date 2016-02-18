from django.conf.urls import url

import experiments.views

urlpatterns = [
    url(r'^/?$', experiments.views.IndexView.as_view(),
        name='experiments.index'),
    url(r'^music_search/?$', experiments.views.MusicSearchView.as_view(),
        name='experiements.music_search'),
]
