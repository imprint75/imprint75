import logging

from django.shortcuts import render
from django.template.defaultfilters import slugify

from home.decorators import login_check
from lib.EchoNest import echo_get_artist, echo_lookup, echo_artist_info

logger = logging.getLogger(__name__)


@login_check
def index(request):
    return render(request, 'index.html', locals())


@login_check
def music_search(request):
    main_search = echo_get_artist(request)
    search_key = slugify(main_search)

    info = {}
    details = echo_lookup(search_key)
    for i in details:
        blogs = echo_artist_info(i['id'], "blogs")
        blogs = blogs if blogs else ["No blogs found"]
        info[i['name']] = blogs

    return render(request, 'experiments/experiments.html', locals())
