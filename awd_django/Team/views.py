from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import viewsets, status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer, UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAdminUser
from awd_django.securetkey import generate_secure_token,create_uuid
from .decoratorts import admin_required
from django.contrib.auth.decorators import login_required

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user,TeamToken=generate_secure_token())
        obj.members.add(self.request.user)
        obj.save()

class TeamList(APIView):
    permission_classes=[IsAdminUser]

    def get(self, request):
        teams=Team.objects.all()
        team_name=[team.name for team in teams]
        data={
        'teamname':team_name,
        'create_by':create_by
        }
        return Response(data)

@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    

    return Response(serializer.data)

@api_view(['POST'])
def join_team(request):
    team_token = request.data.get('TeamToken') 
    team=Team.objects.filter(TeamToken=team_token).first()

    if(team.members.all().count()>team.limit_member-1):
        return Response({'error': 'User Max!'}, status=status.HTTP_400_BAD_REQUEST)
    if(Team.objects.filter(members__username=request.user.username).exists()):
        return Response({'error': 'Already have a team'}, status=status.HTTP_400_BAD_REQUEST)
    user=request.user
    team.members.add(user)

    return Response()




@api_view(['POST'])
def delete_member(request, membername):
    try:
        team = Team.objects.filter(created_by=request.user).first()
        if not team:
            return Response({'error': 'Team does not exist!'})
        if team.created_by.username==membername:
            team.delete()
            return Response({'message': 'The team was deleted'})
            

        member=User.objects.get(username=membername)
        team.members.remove(member)
        return Response({'message': 'The member was deleted'})
    except ObjectDoesNotExist:
        return Response({'error': 'Not Team or Not member'})

