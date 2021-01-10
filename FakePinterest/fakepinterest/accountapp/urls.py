from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp" #간편해짐


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]