from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import Usermember
from .serializers import UsermemberSerializer
from rest_framework.response import Response
#获取排行榜数据
class GetScore(APIView):
    queryset=Usermember.objects.all()
    Usermembers=UsermemberSerializer(queryset)
    def get(self,request):
        queryset=Usermember.objects.all()
        Usermembers=UsermemberSerializer(queryset)
        print(Usermembers)
        data={
            'Users':Usermembers.data
        }
        return Response(data)