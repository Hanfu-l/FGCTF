from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TopicViewSet,submitflag,CreateScore,Statistics


router = DefaultRouter()
router.register('topics',TopicViewSet,basename='topics')


urlpatterns = [
    path('topics/Statistics/',Statistics.as_view(),name="Statistics"),
    path('score/user/', CreateScore,name='createuserscore'),
    path('topics/submitflag/', submitflag,name='submitflag'),
    path('', include(router.urls)),
]
