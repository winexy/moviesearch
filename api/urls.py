from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^search/?', views.search),
    url(r'^movie/?', views.get_details)
]