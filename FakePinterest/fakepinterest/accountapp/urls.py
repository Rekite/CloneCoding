from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp" #간편해짐


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 로그인/로그아웃 (장고 기본제공)
    path('login/', LoginView.as_view(template_name='accountapp/login.html '), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 클래스형뷰는 as_view가 필요
    path('create/', AccountCreateView.as_view(), name='create'),
    # 특정 유저의 정보의 아이디가 필요함(primary key)
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]