from django.contrib.auth.models import User

from rest_framework import serializers

from topic.models import Score


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



class LeaderBoardSerializer(serializers.ModelSerializer):
    Score_by=serializers.CharField(source='Score_by.username')

    class Meta:
        model = Score
        fields=(
            'Score_by',
            'score'
        )