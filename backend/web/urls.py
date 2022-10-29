from django.contrib import admin
from django.urls import path, include
from web import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CPU', views.CPUViewSet)
router.register('AllData', views.AllDataViewSet)
router.register('CPUCooler', views.CPUCoolerViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
