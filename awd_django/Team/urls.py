from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, get_my_team,join_team,delete_member,TeamList

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/delete_member/<str:membername>/', delete_member, name='delete_member'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/join_team/', join_team, name='join_team'),
    path('teams/list_team/', TeamList.as_view(), name='team_list'),
    path('', include(router.urls)),
]