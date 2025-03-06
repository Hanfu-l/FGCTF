from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import is_standing,SetingUsers,GetLeaderBoard

urlpatterns = [
    path('control/is_standing/', is_standing, name='is_standing'),
    path('Seting/SetingUsers/',SetingUsers.as_view(),name='SetingUsers'),
    path('GetLeaderBoard/',GetLeaderBoard,name='GetLeaderBoard')
]