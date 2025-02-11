from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GetScore

urlpatterns = [
    path('user/getscore/', GetScore.as_view(), name='getscore'),
]

