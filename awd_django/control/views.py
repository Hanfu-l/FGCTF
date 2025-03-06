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
from .serializers import UserSerializer,LeaderBoardSerializer

from topic.models import Score


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


#是否是管理员
@api_view(['POST'])
def is_standing(request):
    return Response({'isadmin': request.user.is_superuser})



#获取用户积分排行榜
@api_view(['GET'])
def GetLeaderBoard(request):
    queryset=Score.objects.all().order_by('-score')
    serializers=LeaderBoardSerializer(queryset,many=True)
    return Response(serializers.data)
