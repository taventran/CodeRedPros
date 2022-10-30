from rest_framework import serializers
from web import models

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motherboard
        fields = ('name', 'price', 'size')

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPU
        fields = ('name', 'price', 'coreCount', 'clockSpeed',)

class CPUCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPUCooler
        fields = ("name", "price")

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Memory
        fields = ("name", "price", "gigs")

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = ('ssd', 'price', 'name', "capacity")

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GPU
        fields = ('price', 'name', "memory", "coreClock")
    
class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerSupply
        fields = ('price', 'name', "watts", "effiency")

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = ('price', 'name', 'size')

class AllDataSerializer(serializers.ModelSerializer):
    CPU = CPUSerializer(many=True, required=False)
    CPUCooler = CPUCoolerSerializer(many=True, required=False)
    memory = MemorySerializer(many = True, required = False)
    storage = StorageSerializer(many = True, required = False)
    GPU = GPUSerializer(many = True, required = False)
    powerSupply = PowerSupplySerializer(many = True, required = False)
    case = CaseSerializer(many = True, required = False)

    class Meta:
        model = models.AllData
        fields = ('CPU', 'CPUCooler', 'memory', 'storage', 'GPU', 'powerSupply', 'case',)

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = ('use', 'aesthetic', 'priceRange', 'size', 'image_url')