from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    # set_null=유저가 사라졌을 때 게시글이 사라지지 않고 남아있음
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)