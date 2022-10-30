from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from web import serializers
from web import models
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer
    parser_classes = (MultiPartParser, FormParser)
    @action(detail=True, methods=["POST"])
    def makeUserData(self, request, pk=None):
        if 'use' and 'aesthetic' and 'priceRange' and 'size' in request.data:
            use = request['use']
            aesthetic = request['aesthetic']
            priceRange = request['priceRange']
            size = request['size']
            serializer = serializers.UserDataSerializer
            Data = models.UserData.objects.create(use=int(use), aesthetic=int(aesthetic), 
                priceRange=float(priceRange), size=int(size))
            Data.save()
            response = {'message': 'New data', 'result':serializer.data}
            return Response(response, status.HTTP_200_OK)
        else:
            response = {'message': 'Missing info'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = models.Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer

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

