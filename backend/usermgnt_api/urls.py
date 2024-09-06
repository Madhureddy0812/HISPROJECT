
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *


router = DefaultRouter()
router.register('userData',userDataModelViewSet,basename='user_data')

urlpatterns = [
   
    path('',include(router.urls)),
   
]