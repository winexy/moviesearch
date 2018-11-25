# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('password', models.CharField(max_length=30, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
            ],
        ),
        migrations.CreateModel(
            name='UserMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(verbose_name='imdbID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]
