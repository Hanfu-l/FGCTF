from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TopicViewSet,CreateScore,Statistics,GetTopicData,GetTopicList,DockerRun,CloseDocker,GetRunDocker,SubmitFlag


router = DefaultRouter()
router.register('topics',TopicViewSet,basename='topics')

urlpatterns = [
    path('topics/Statistics/',Statistics.as_view(),name="Statistics"),
    path('score/user/', CreateScore,name='createuserscore'),
    path('Topic/GetTopic/<int:TopicId>',GetTopicData,name='GetTopicData'),
    path('Topic/List',GetTopicList,name='GetTopicList'),
    path('Topic/RunTopic',DockerRun,name='DockerRun'),
    path('Topic/CloseTopic',CloseDocker,name='CloseDocker'),
    path('Topic/GetRunDocker',GetRunDocker,name='GetRunDocker'),
    path('Topic/SubmitFlag',SubmitFlag,name='SubmitFlag'),
    path('', include(router.urls)),
]
