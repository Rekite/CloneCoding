from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp" #간편해짐


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # 클래스형뷰는 as_view가 필요
    path('create/', AccountCreateView.as_view(), name='create'),

]