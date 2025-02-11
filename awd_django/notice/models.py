from django.db import models
# Create your models here.
#公告模型
class Notice(models.Model):
    name = models.CharField(max_length=30,unique=True)
    Description=models.CharField(max_length=255)
    Visable=models.BooleanField(default=False)