# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-15 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181209_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermovies',
            name='movie_id',
            field=models.CharField(max_length=50, verbose_name='imdbID'),
        ),
    ]