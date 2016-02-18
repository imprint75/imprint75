import logging

from django.shortcuts import render
from django.views.generic import View

logger = logging.getLogger(__name__)


class IndexView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


def info(request):
    message = "Info"
    return render(request, 'common/base.html', locals())
