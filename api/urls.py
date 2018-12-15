from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^search/?', views.search),
    url(r'^movie/?', views.get_details),
    url(r'^auth/login/?', views.login),
    url(r'^auth/registration/?', views.register),
    url(r'^like/?', views.like),
    url(r'^get_user_movies/?', views.get_user_movies)
]