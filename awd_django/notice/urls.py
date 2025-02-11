from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet,getnotice


router = DefaultRouter()
router.register('notice',NoticeViewSet,basename='notices')


urlpatterns = [
    path('notices/list/', getnotice,name='getnotice'),
    path('', include(router.urls)),
    
]
