from django.contrib.auth.models import User
from django.db import models



class Team(models.Model):
    name = models.CharField(max_length=30,unique=True)
    limit_member=models.IntegerField(default=3,editable=False)
    members = models.ManyToManyField(User, related_name='teams')
    score=models.IntegerField(default=0)
    TeamToken=models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class information(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='messages')
    name = models.CharField(max_length=30,unique=True)
    is_delete=models.BooleanField(default=True)
    content=models.CharField(max_length=255,null=False)
    created_by = models.ForeignKey(User, related_name='created_infomation',on_delete=models.CASCADE)
    