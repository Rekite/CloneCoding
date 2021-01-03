from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL #setting에 기본적으로 있음

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Tweet(models.Model):
    #리트윗할 때만 parent가 존재함
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL) # SET_NULL => referencing한 트윗이 없어졌을 때 여기 트윗도 null로 바꿈
    #id = models.AutoField(primary_key=True)
    # cascade 안하고 싶으면(계정 이력 남기고 싶을 때) null=True, on_delete=models.set_null하면 됨
    # 또한 유저가 사라져도 트윗 남기고 싶을 때 사용함
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many users can have many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id'] #-id -> 역순


    # parent가 있으면 retweet임
    @property
    def is_retweet(self):
        return self.parent != None


    #없어져도 되는 부분
    def serialize(self):
        return{
            'id':self.id,
            'content':self.content,
            'likes': random.randint(0, 200)
        }