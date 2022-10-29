from django.forms import modelformset_factory
from rest_framework import serializers
from web import models


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPU
        fields = ('name', 'price', 'coreCount', 'performanceCoreClock',)

class CPUCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPUCooler
        fields = ("name", "price")

class AllDataSerializer(serializers.ModelSerializer):
    CPU = CPUSerializer(many=True, required=False)
    CPUCooler = CPUCoolerSerializer(many=True, required=False)
    class Meta:
        model = models.AllData
        fields = ('CPU', 'CPUCooler')
