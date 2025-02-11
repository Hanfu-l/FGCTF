from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Competition,Flag,Topic
from Team.serializers import TeamSerializer,UserSerializer
from Team.models import Team

class CompetitionSerializer(serializers.ModelSerializer):
    teams =TeamSerializer(read_only=True)
    token = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Competition
        fields = (
            "id",
            "name",
            "starttime",
            "rounttime",
            "rountnumber",
            "currentrount",
            "flagformat",
            "endtime",
            "token",
            "teams",
            "rounttimelist",
            "IsActivate",
        )

class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = (
            "value",
            "starttime",
            "endtime",
            "IsEffective",
            "competition",
            "team",
            "topic",
        )

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields=(
            'attackscore',
            'checkscore',
            'initscore',
            'name',
            'external',
            'interior',
            'interiorpath',
            'sshname',
            'sshpassword',
            'flagpath',
            'competition',
        )