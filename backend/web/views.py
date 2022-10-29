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

class CPUCoolerViewSet(viewsets.ModelViewSet):
    queryset = models.CPUCooler.objects.all()
    serializer_class = serializers.CPUCoolerSerializer

class AllDataViewSet(viewsets.ModelViewSet):
    queryset = models.AllData.objects.all()
    serializer_class = serializers.AllDataSerializer