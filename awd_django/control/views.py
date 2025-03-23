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
from .LangGPT import GPTV1

from .RedisControl import RedisClass,LeaderBoard
from django.core.cache import cache
from django_redis import get_redis_connection

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
    RedisLeader=LeaderBoard()
    if not RedisLeader.if_leaderboard():
        queryset=Score.objects.all().order_by('-score')
        serializers=LeaderBoardSerializer(queryset,many=True)
        for userdata in serializers.data:
            RedisLeader.add_user(userdata['Score_by'],userdata['score'])
    resdata=RedisLeader.get_rank()
    return Response(resdata)

#获取用户信息
@api_view(['GET'])
def GetMyData(request):
    user=request.user
    user_score=Score.objects.filter(Score_by=user).first()
    RedisLeader=LeaderBoard()
    rank=RedisLeader.get_user_leaderboard(str(user))

    jsondata={'username':str(user),'score':user_score.score,'rank':rank}

    return Response(jsondata)


#LangChain接口
@api_view(['POST'])
def GPT(request):
    data=request.data
    user=request.user
    Redis=RedisClass()

    ChatLock=f"chat_lock:{user}"

    if not Redis.Create_Lock(ChatLock):
        return Response("Chat is starting,Please wait...")


    try:

        question=data['question']
        res=GPTV1(str(question))
        userquestionskey=f"ChatQuestion:{user}"
        Redis.Put_Questions(userquestionskey,question,res)
        return Response("200")

    finally:
        Redis.Delete_Lock(ChatLock)


@api_view(['GET'])
def GetQuestions(request):
    user=request.user
    userquestionskey=f"ChatQuestion:{user}"
    Redis=RedisClass()
    quedata=Redis.Get_QuestionsData(userquestionskey)
    return Response(quedata)