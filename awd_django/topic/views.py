from django.shortcuts import render


from django.db import transaction
import docker.errors
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import Topic,Score,UserDockerData
from .serializers import TopicSerializer,TopicListSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

from django.http import JsonResponse
from django.core.cache import cache

from datetime import datetime

import docker
from docker.errors import NotFound
import hashlib


from .redis_pool import PortPool

# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class=TopicSerializer
    queryset = Topic.objects.all()

@api_view(['GET'])
def CreateScore(request):
     user=request.user
     Keyuser=User.objects.filter(username=user).first()
     ifscore=Score.objects.filter(Score_by=Keyuser).first()
     print(Keyuser.first_name)
     if Keyuser.first_name=="":
          Keyuser.first_name=123
          Keyuser.save()
          print(Keyuser.first_name)
     else:
          data1=Keyuser.first_name
          data2=int(data1)
          data3=data2+100
          data4=str(data3)
          Keyuser.first_name=data4
          Keyuser.save()
          return Response({'message': 'Score True'})
     

class Statistics(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        TopicNumber=Topic.objects.count()
        UserNumber=User.objects.count()

        data={
            'TopicNumber':TopicNumber,
            'UserNumber':UserNumber,

        }
        return Response(data)



#前端获取题目信息，返回名称，分数，描述
@api_view(['GET'])
def GetTopicData(request,TopicId):
     searchid=int(TopicId)
     topics=Topic.objects.filter(pk=searchid).first()
     serializers=TopicListSerializer(topics)
     return Response(serializers.data)



@api_view(['GET'])
def GetTopicList(request):
     topics=Topic.objects.all().values('pk','name','score','Description')
     serializers=TopicListSerializer(topics,many=True)
     return Response(serializers.data)



#启动Docker镜像
@api_view(['POST'])
def DockerRun(request):
     user=request.user

     #锁
     lock_key=f"user_docker_lock:{user}"
     Port=PortPool()

     userdata=User.objects.filter(username=user).first()
     user_docker_data,created=UserDockerData.objects.get_or_create(DockerUser=user)

     if not Port.Put_Docker_Lock(lock_key):
          return Response("Docker is starting,Please wait...")

     try:

          if user_docker_data.RunDockerNumber==0:
               #镜像名称md5编码
               md5=hashlib.md5()
               seed=str(userdata.first_name)+str(datetime.timestamp(datetime.now()))
               md5.update(seed.encode('utf-8'))
               dockername=md5.hexdigest()


               #获取题目信息
               topicid=request.data['topicid']
               topicdata=Topic.objects.filter(pk=topicid).first()

               client=docker.from_env()

               container=client.containers.run(
                    topicdata.DockerName,
                    name=dockername,
                    detach=True,
                    ports={topicdata.DockerPort:str(Port.get_available_port(),'utf-8')}
               )
               with transaction.atomic():
                    user_docker_data.RunDockerNumber=1
                    user_docker_data.RunDockerId=dockername
                    user_docker_data.RunDockerTopicId=topicid
                    user_docker_data.save()

               return Response("Docker Run Success")
          else:
               return Response("User RunDocker Max")
     except docker.errors.DockerException as e:
          error_message=str(e)
          return Response(f"Docker Run Fail : {error_message}")
    
     finally:
          Port.Delete_Docker_Lock(lock_key)


#获取当前启动镜像的信息
@api_view(['GET'])
def GetRunDocker(request):
     user=request.user
     client=docker.from_env()

     user_docker_data,created=UserDockerData.objects.get_or_create(DockerUser=user)


     if user_docker_data.RunDockerNumber>0:

          try:
            # 尝试获取容器
            container = client.containers.get(user_docker_data.RunDockerId)
            
            res={
                 'RunDockerTopicId':user_docker_data.RunDockerTopicId,
                 'RunDockerUrl':'http://192.168.245.136',
                 'RunDockerPort':container.attrs['NetworkSettings']['Ports']['80/tcp'][0]['HostPort']
            }

          except NotFound:
            # 未能捕捉到当前名字的容器启动
               user_docker_data.RunDockerTopicId=-1
               user_docker_data.RunDockerNumber=0
               user_docker_data.save()

          return Response(res)
     else:
          return Response("No image is currently running")

#TopicDes界面的镜像显示
@api_view(['POST'])
def ImageVisable(request):
     pass


#关闭当前启动的镜像
@api_view(['GET'])
def CloseDocker(request):
     user=request.user
     client=docker.from_env()
     try:
          user_docker_data,created=UserDockerData.objects.get_or_create(DockerUser=user)
          container=client.containers.get(user_docker_data.RunDockerId)
          container.remove(force=True)

          user_docker_data.RunDockerTopicId=-1
          user_docker_data.RunDockerNumber=0
          user_docker_data.save()
          return Response("Docker Close")
     except docker.errors.ImageNotFound:
          return Response("Container does not exist")

     except docker.errors.APIError as e:
          return Response("Error while deleting")



#提交题目Flag
@api_view(['POST'])
def SubmitFlag(request):
     data=request.data
     submittopic=Topic.objects.filter(pk=data['topicid']).first()
     print(data)
     print(data['submitflag'])
     print(submittopic.Keyvalue)
     if data['submitflag'] == submittopic.Keyvalue:
          user=request.user
          Keyuser=User.objects.filter(username=user).first()
          score=user.UserScore
          score.add_topic(submittopic)

          return Response('Flag right')

     else:
          return Response('Flag error')