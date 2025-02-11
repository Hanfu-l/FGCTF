from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

from .decorator import admin_required
from .serializers import UserSerializer,CompetitionSerializer,TopicSerializer

from Team.models import Team
from competition.models import Competition,Topic


from datetime import datetime,timedelta
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

#Check机制
class CheckDown(APIView):
    permission_classes=[IsAdminUser]

#攻击得分
class SubmitFlag(APIView):
    pass

#靶机初始化
class InitDocker(APIView):
    permission_classes=[IsAdminUser]




#获取全部用户
class SetingUsers(APIView):
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    Users=UserSerializer(queryset)

    def get(self,request):
        queryset=User.objects.all()
        Users=UserSerializer(queryset,many=True)
        data={
            'Users':Users.data
        }

        return Response(data)
class Leader(APIView):
    queryset=User.objects.all().order_by('-first_name')
    Users=UserSerializer(queryset)

    def get(self,request):
        queryset=User.objects.all().order_by('-first_name')
        Users=UserSerializer(queryset,many=True)
        data={
            'Users':Users.data
        }

        return Response(data)
#获取全部团队
class SetingTeams(APIView):
    permission_classes=[IsAdminUser]
    queryset=Team.objects.all()
    Users=UserSerializer(queryset)

    def get(self,request):
        queryset=User.objects.all()
        Users=UserSerializer(queryset,many=True)
        data={
            'Users':Users.data
        }

        return Response(data)

class SetingCompetitions(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        queryset=Competition.objects.all()
        Competitions=CompetitionSerializer(queryset,many=True)
        data={
            'Competitions':Competitions.data
        }
        
        return Response(data)

class Statistics(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        TeamNumber=Team.objects.count()
        TopicNumber=Topic.objects.count()
        UserNumber=User.objects.count()
        CompetitionNumber=Competition.objects.count()
        data={
            'TeamNumber':TeamNumber,
            'TopicNumber':TopicNumber,
            'UserNumber':UserNumber,
            'CompetitionNumber':CompetitionNumber
        }
        return Response(data)

class GetCompetition(APIView):
    permission_classes=[IsAdminUser]

    def post(self,request):
        token=request.data.get('token')
        Com=Competition.objects.filter(token=token).first()
        DataCom=CompetitionSerializer(Com)
        data={
            'data':DataCom.data
        }
        return Response(data)

class TopicAdd(APIView):
    permission_classes=[IsAdminUser]

    def post(self,request):
        serializer=TopicSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response("Success")

def start_scheduler(CompetitionID):
    Com=Competition.objects.filter(pk=CompetitionID).first()
    sche=BackgroundScheduler()
    interval=IntervalTrigger(seconds=Com.rounttime.seconds)
    sche.add_jobstore(DjangoJobStore(),"default")
    sche.add_job(Topic_monitor,trigger=interval,next_run_time=Com.starttime,args=[CompetitionID],id=Com.token)
    sche.start()
    print(Com.rounttime)
    print(Com.starttime)
    
def Topic_monitor(CompetitionID):
    Com=Competition.objects.filter(pk=CompetitionID).first()
    print(datetime.now())
    
    

class ApschedulerAdd(APIView):
    
    def post(self,request):
        
        CompetitionID=request.data.get('CompetitionID')
        start_scheduler(CompetitionID)
        
        return Response("Success")


#是否是管理员
@api_view(['POST'])
def is_standing(request):
    return Response({'isadmin': request.user.is_superuser})


