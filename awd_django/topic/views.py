from django.shortcuts import render

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import Topic,Notice,Score
from .serializers import TopicSerializer,NoticeSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class=TopicSerializer
    queryset = Topic.objects.all()

@api_view(['POST'])
def submitflag(request):
    flag=request.data['flag']
    iftopic=Topic.objects.filter(Keyvalue=flag).first()
    Keyuser=User.objects.filter(username=request.user).first()
    if not iftopic:
         print("1")
         return Response({'error': 'Flag inaccuracy'})
    else:
         data1=Keyuser.first_name
         data2=int(data1)
         data3=iftopic.score
         data4=data2+data3
         Keyuser.first_name=data4
         Keyuser.save()
         print(Keyuser.first_name)
         return Response({'message': 'Flag True'})

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
          print(Keyuser.first_name)
          print("不为0")
          return Response({'message': 'Score True'})
     '''
     if not ifscore:
          Score.objects.create(Score_by=Keyuser)
          return Response({'message': 'Score True'})
     else:
        return Response({'message': 'Score always'})
     '''
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
