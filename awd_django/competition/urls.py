from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CompetitionViewSet,CompetitionList,join_competition,CompetitionInit,TopicViewSet,CompetitionOpen,GetAttackDefense
router = DefaultRouter()
router.register('competitions', CompetitionViewSet, basename='competitions')
router2=DefaultRouter()
urlpatterns = [
    path('competitions/opencompetition/', CompetitionOpen.as_view(), name='CompetitionOpen'),
    path('competitions/initcompetition/', CompetitionInit.as_view(), name='CompetitionInit'),
    path('competitions/join_competition/', join_competition, name='join_competition'),
    path('competitions/list_competition/', CompetitionList.as_view(), name='list_competition'),
    path('competitions/attackdefense/', GetAttackDefense.as_view(), name='attackdefense'),
    path('', include(router.urls)),
]