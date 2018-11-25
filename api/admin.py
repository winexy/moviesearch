# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import User, UserMovies
# Register your models here.

admin.site.register(User)
admin.site.register(UserMovies)