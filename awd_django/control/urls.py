from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import is_standing,SetingUsers,Statistics,SetingCompetitions,GetCompetition,TopicAdd,ApschedulerAdd,Leader

urlpatterns = [
    path('control/is_standing/', is_standing, name='is_standing'),
    path('Seting/SetingUsers/',SetingUsers.as_view(),name='SetingUsers'),
    path('Seting/Leader/',Leader.as_view(),name='Leader'),
    path('Seting/SetingCompetitions/',SetingCompetitions.as_view(),name='SetingCompetitions'),
    path('Seting/SetingCompetitions/GetCompetition/',GetCompetition.as_view(),name='GetCompetition'),
    path('Seting/SetingCompetitions/Competition/TopicAdd/',TopicAdd.as_view(),name='TopicAdd'),
    path('Seting/SetingCompetitions/Competition/ApschedulerAdd/',ApschedulerAdd.as_view(),name='ApschedulerAdd'),
    

]