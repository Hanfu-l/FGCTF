from django.shortcuts import render

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework.decorators import api_view,action

from rest_framework.response import Response
# Create your views here.
class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class=NoticeSerializer
    queryset = Notice.objects.all()


@api_view(['GET'])
def getnotice(request):
    notices=Notice.objects.all().filter(Visable=True)
    ser=NoticeSerializer(notices,many=True)
    return Response(ser.data)