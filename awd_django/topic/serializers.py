from rest_framework import serializers

from .models import Topic

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


class TopicListSerializer(serializers.ModelSerializer):
     class Meta:
        model = Topic
        fields =(
            "pk",
            "name",
            "score",
            "Description",
        )



