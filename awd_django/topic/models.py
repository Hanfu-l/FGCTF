from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
#题目模型
class Topic(models.Model):
    name = models.CharField(max_length=30,unique=True)
    score=models.IntegerField(default=0)
    DockerName=models.CharField(max_length=255)
    DockerPort=models.CharField(max_length=255)
    UrlPath=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    Visable=models.BooleanField(default=False)
    Keyvalue=models.CharField(max_length=255,default="123")

#公告模型
class Notice(models.Model):
    name = models.CharField(max_length=30,unique=True)
    Description=models.CharField(max_length=255)
    Visable=models.BooleanField(default=False)


class Score(models.Model):
    Score_by = models.ForeignKey(User, related_name='UserScore',on_delete=models.CASCADE)
    score=models.IntegerField(default=0)