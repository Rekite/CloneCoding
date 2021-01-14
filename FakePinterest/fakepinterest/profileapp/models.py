from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # profile과 user객체를 하나씩 연결해줌
    # on_delete => 연결된 user객체가 없어질 때 profile이 어떤 행동을 보일지
    # related_name : 굳이 profile객체를 찾지 않더라도 이 user의 profile에 (request.user.profile과 같이 연결할 수 있도록 해줌)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # media 밑에 profile 경로가 추가돼서 그 안에 업로드됨
    image = models.ImageField(upload_to='profile/', null=True)
    # unique : profile객체에서 nickname은 하나가 유일해야 함
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)