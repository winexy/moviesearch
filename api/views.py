# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from movieapi.settings import OMDB_API
from django.http import HttpResponse, QueryDict
from api.models import User, UserMovies
from django.core.serializers import serialize
import requests
import json

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


def login(request):
    data = json.loads(request.body)

    user = User.objects.get(login=data.get('login'))
    data = serialize('json', [user, ])
    data = json.loads(data)
    data = {
        'id': data[0]['pk'],
        'login': data[0]['fields']['login']
    }

    data = json.dumps(data)

    return HttpResponse(data)


def register(request):
    data = json.loads(request.body)
    user = User(**data)
    try:
        user.save()
        return HttpResponse(user.id)
    except:
        return HttpResponse('user with such login already registered')


def like(request):
    like = request.GET.get('like')
    movie_id = request.GET.get('id')
    user_id = request.GET.get('user')

    try:
        user_movie = UserMovies.objects.get(movie_id=movie_id)
        print user_movie
        if like == "false":
            user_movie.delete()
            return HttpResponse(0)
    except:
        if like == "true":
            user_movie = UserMovies(movie_id=movie_id, user_id=user_id)
            user_movie.save()
            return HttpResponse(1)

    return HttpResponse(0)


def get_user_movies(request):
    user_id = request.GET.get('user')
    movies = UserMovies.objects.filter(user_id=user_id)
    return HttpResponse(serialize('json', movies))

