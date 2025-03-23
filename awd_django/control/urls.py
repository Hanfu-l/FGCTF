from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import is_standing,SetingUsers,GetLeaderBoard,GPT,GetQuestions,GetMyData

urlpatterns = [
    path('control/is_standing/', is_standing, name='is_standing'),
    path('Seting/SetingUsers/',SetingUsers.as_view(),name='SetingUsers'),
    path('GetLeaderBoard/',GetLeaderBoard,name='GetLeaderBoard'),
    path('GPT',GPT,name="GPT"),
    path('GetQuestions',GetQuestions,name="GetQuestions"),
    path('GetMydata',GetMyData,name="GetMyData"),
    
]