from django.contrib import admin
from django.urls import path, include
from web import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('userdata', views.UserDataViewSet)
router.register('motherboard', views.MotherboardViewSet)
router.register('CPU', views.CPUViewSet)
router.register('powersupply', views.PowerSupplyViewSet)
router.register('AllData', views.AllDataViewSet)
router.register('CPUCooler', views.CPUCoolerViewSet)
router.register('memory', views.MemoryViewSet)
router.register('storage', views.StorageViewSet)
router.register('GPU', views.GPUViewSet)
router.register('case', views.CaseViewSet)
router.register('outputcomputer', views.OutputComputerViewSet)


urlpatterns = [
    path('api/', include(router.urls))
] 
