from datetime import datetime,timedelta
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler

import paramiko

from awd_django.securetkey import generate_secure_token,create_uuid
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Team.serializers import TeamSerializer
from .models import Competition,Flag,Topic
from .serializers import CompetitionSerializer,FlagSerializer,TopicSerializer


from Team.models import Team


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=TopicSerializer
    queryset=Topic.objects.all()
    


class CompetitionViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=CompetitionSerializer
    queryset=Competition.objects.all()


    def perform_create(self, serializer):
        CompetitionToken=generate_secure_token()
        obj = serializer.save(token=CompetitionToken)
        obj.save()

class CheckFlag(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        flagvalue=request.data.get('flagvalue')
        

class GetAttackDefense(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
            Token=request.data.get('token')
            team=Team.objects.filter(members=request.user).first()
            Com=Competition.objects.filter(teams=team,token=Token).first()
            topic=Topic.objects.filter(team=team,competition=Com)
            data={
              "Competition":CompetitionSerializer(Com).data,
              "Topic":TopicSerializer(topic,many=True).data,
            }
            return Response(data)
       

def get_team_rank(team):
    all_teams=Team.objects.all().order_by('-score')
    rank = next((index + 1 for index, t in enumerate(all_teams) if t == team), None)
    return rank

class CompetitionList(APIView):
    permission_classes=[IsAdminUser]

    def get(self, request):
        Competitions=Competition.objects.all()
        Conser=CompetitionSerializer(Competitions,many=True)
        data={
            'data':Conser.data,
        }
        return Response(data)


#初始化竞赛
class CompetitionInit(APIView):
    permission_classes=[IsAdminUser]

    def post(self,request):
        Token=request.data.get('CompetitionToken')
        CreateFlag(Token)
        Com=Competition.objects.filter(token=Token).first()
        Com.IsActivate=True
        Com.save()
        InitTopic(Token)
        return Response()


#生成Flag
def CreateFlag(token):
    Com=Competition.objects.filter(token=token).first()
    Flag_delete=Flag.objects.filter(competition=Com)
    Flag_delete.delete()
    Top=Topic.objects.filter(competition=Com)
    if Com.IsActivate==True:
        for topic in Top:
            timelist=Com.rounttimelist()
            for team in Com.teams.all():
                for i in range(0,len(timelist)-1):         
                    flagvalue=Com.flagformat+'{'+create_uuid()+'}'
                    FlagData={
                        'starttime':timelist[i],
                        'endtime':timelist[i+1],
                        'value':flagvalue,
                        'team':team.id,
                        'competition':Com.id,
                        'topic':topic.pk,
                    }
                    flag_serializer = FlagSerializer(data=FlagData)
                    if flag_serializer.is_valid():
                        flag_serializer.save()
                        flag=Flag.objects.filter(value=flagvalue).first()
                    else:
                        print(f"Invalid data for flag {i}: {flag_serializer.errors}")
    else:
        return Response({'error': 'Competition is Activated!'})
                
#自动分配题目信息
def InitTopic(ComToken):
    Com=Competition.objects.filter(token=ComToken).first()
    Topics=Topic.objects.filter(competition=Com)
    for team in Com.teams.all():
         for topic in Topics:
            topic.team=team
            topic.save()
    print("分配完毕")


class CompetitionOpen(APIView):
    permission_classes=[IsAdminUser]

    def post(self,request):
        Token=request.data.get('CompetitionToken')
        SSHTopic(Token)
        return Response()

def SSHTopic(ComToken):
    Com=Competition.objects.filter(token=ComToken).first()
    if Com:
        for team in Com.teams.all():
            Topicdata=Topic.objects.filter(team=team)
            if Topicdata:
                for topic in Topicdata:
                    try:
                        sshdata=topic.interior
                        sshdata=sshdata.split(':')
                        ssh_client=paramiko.SSHClient()
                        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh_client.connect(hostname=sshdata[0],port=sshdata[1], username=topic.sshname, password=topic.sshpassword,timeout=4)
                        cmd = 'echo "{}" > {}flag.txt'.format(getflag(topic.pk),topic.interiorpath)
                        print(cmd)
                        stdin, stdout, stderr = ssh_client.exec_command(cmd)
                        ssh_client.close()
                    except:
                        print(topic.interior+"&"+topic.sshname+"&"+topic.sshpassword)
                        continue
            
def getflag(topicpk):
    topic=Topic.objects.filter(pk=topicpk).first()
    current_time = timezone.now()
    flag=Flag.objects.filter(team=topic.team,competition=topic.competition,starttime__lte=current_time, endtime__gte=current_time).first()
    if flag:
        print(flag.value)
        return flag.value
    else:
        return " "
    

    
    

#竞赛监视器
def Supervisor(Comtoken):
     Com=Competition.objects.filter(token=Comtoken).first()
     


    


@api_view(['POST'])
def join_competition(request):
    team = Team.objects.filter(created_by=request.user).first()
    print(team.name)
    if not team:
        return Response({'error': 'Team does not exist!'})
    else:
        CompetitionToken=request.data.get('CompetitionToken')
        Com=Competition.objects.filter(token=CompetitionToken).first()
        print(Com.name)
        if not Com:
            return Response({'error': 'Competition does not exist!'})
        else:
            Com.teams.add(team)
            print(Com.teams.all())
            return Response({'message': 'Team added'})

class TopicSSH(APIView):
    permission_classes=[IsAdminUser]

    def post(self,request):
        pass
    