import logging

from django.shortcuts import render

from home.decorators import login_check

logger = logging.getLogger(__name__)

@login_check
def index(request):
    return render(request, 'home.html', locals())

@login_check
def info(request):
    message = "Info"
    return render(request, 'common/base.html', locals())
