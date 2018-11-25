# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=30, verbose_name='Логин')
    password = models.CharField(max_length=30, verbose_name='Пароль')

    def __str__(self):
        return self.login


class UserMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField(verbose_name='imdbID')

