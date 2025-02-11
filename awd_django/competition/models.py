from django.db import models
from django.utils import timezone
from Team.models import Team
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Competition(models.Model):
    name = models.CharField(max_length=30,unique=True)
    token=models.CharField(max_length=50)
    teams=models.ManyToManyField(Team,related_name='competitions')
    starttime=models.DateTimeField(null=False)
    rounttime=models.DurationField(null=False)
    rountnumber=models.PositiveIntegerField(default=12)
    currentrount=models.IntegerField(default=0)
    flagformat=models.CharField(max_length=10,default="flag")
    IsActivate=models.BooleanField(default=False)

    def endtime(self):
        end_time=self.starttime+(self.rountnumber* self.rounttime*60)
        return(end_time)
    
    def rounttimelist(self):
        timelist=[]
        for i in range(0,self.rountnumber+1):
            timelist.append(self.starttime+(self.rounttime*i*60))
        return timelist

    def __str__(self):
        return self.name



class Topic(models.Model):
    attackscore=models.IntegerField(default=100)
    checkscore=models.IntegerField(default=100)
    initscore=models.IntegerField(default=1000)
    name = models.CharField(max_length=30,null=False)
    team = models.ForeignKey(Team, related_name='topics', on_delete=models.CASCADE,null=True)
    competition= models.ForeignKey(Competition, related_name='topics', on_delete=models.CASCADE,null=True)
    external=models.CharField(max_length=255)
    interior=models.CharField(max_length=255)
    interiorpath=models.CharField(max_length=255,null=False)
    sshname=models.CharField(max_length=30)
    sshpassword=models.CharField(max_length=30)
    flagpath=models.CharField(max_length=255,null=False)

class Flag(models.Model):
    value=models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, related_name='flags', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='flags', on_delete=models.CASCADE)
    competition= models.ForeignKey(Competition, related_name='flags', on_delete=models.CASCADE)
    starttime=models.DateTimeField(null=False)
    endtime=models.DateTimeField(null=False)
    def IsEffective(self,time):
        return self.starttime<=time<=self.endtime

