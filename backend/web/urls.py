from django.contrib import admin
from django.urls import path, include
from web import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cpu', views.CPUViewSet)
router.register('AllData', views.AllDataViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
