from rest_framework import serializers

from .models import Topic,Notice

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields =(
            "name",
            "score",
            "DockerName",
            "DockerPort",
            "UrlPath",
            "Description",
            "Visable",
            "Keyvalue",
        )


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields ={
            "name",
            "Description",
            "Visabel",
        }