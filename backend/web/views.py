from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from web import serializers
from web import models

# Create your views here.
class CPUViewSet(viewsets.ModelViewSet):
    queryset = models.CPU.objects.all()
    serializer_class = serializers.CPUSerializer

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = models.Memory.objects.all()
    serializer_class = serializers.MemorySerializer

class CPUCoolerViewSet(viewsets.ModelViewSet):
    queryset = models.CPUCooler.objects.all()
    serializer_class = serializers.CPUCoolerSerializer

class StorageViewSet(viewsets.ModelViewSet):
    queryset = models.Storage.objects.all()
    serializer_class = serializers.StorageSerializer

class GPUViewSet(viewsets.ModelViewSet):
    queryset = models.GPU.objects.all()
    serializer_class = serializers.GPUSerializer

class PowerSupplyViewSet(viewsets.ModelViewSet):
    queryset = models.PowerSupply.objects.all()
    serializer_class = serializers.PowerSupplySerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = models.Case.objects.all()
    serializer_class = serializers.CaseSerializer

class AllDataViewSet(viewsets.ModelViewSet):
    queryset = models.AllData.objects.all()
    serializer_class = serializers.AllDataSerializer