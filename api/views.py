# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from movieapi.settings import OMDB_API
from django.http import HttpResponse, QueryDict
import requests

def search(request):
    query = QueryDict(request.GET.urlencode())
    params = {
        's': query.get('value')
    }
    movies = requests.get(OMDB_API, params=params)
    return HttpResponse(movies)


def get_details(request):
    query = QueryDict(request.GET.urlencode())
    params = {
        'i': query.get('id')
    }
    movie = requests.get(OMDB_API, params=params)
    return HttpResponse(movie)
