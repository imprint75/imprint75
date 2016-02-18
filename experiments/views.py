import logging

from django.shortcuts import render
from django.views.generic import View

from libs.EchoNest import echo_get_artist, echo_lookup, echo_artist_info

logger = logging.getLogger(__name__)


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


class MusicSearchView(View):
    template_name = 'experiments/experiments.html'

    def get(self, request, *args, **kwargs):
        info = self.artist_lookup(request)
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        info = self.artist_lookup(request)
        return render(request, self.template_name, locals())

    def artist_lookup(self, request):
        info = {}
        details = echo_lookup(echo_get_artist(request))
        for i in details:
            blogs = echo_artist_info(i['id'], "blogs")
            blogs = blogs if blogs else ["No blogs found"]
            info[i['name']] = blogs
        return info
