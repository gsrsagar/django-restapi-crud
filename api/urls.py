from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet ,ProductViewSet

router=routers.DefaultRouter()
router.register('movie',MovieViewSet)
router.register('Product',ProductViewSet)
'''urlpatterns = [
    
] '''

urlpatterns=router.urls