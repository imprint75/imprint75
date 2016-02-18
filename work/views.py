from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'work/work.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())
