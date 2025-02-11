from django.contrib.auth.models import User

from rest_framework import serializers

from Team.models import Team
from Team.serializers import TeamSerializer

from competition.models import Competition,Topic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "email"
        )


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

