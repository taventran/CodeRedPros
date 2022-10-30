from unittest.util import _MAX_LENGTH
from django.db import models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create your models here.

def upload_to(instance, filename):
    return f'images/{filename}'

class UserData(models.Model):
    use = models.IntegerField(default = 1, blank = False)
    aesthetic = models.BooleanField(default=False)
    priceRange = models.FloatField(default=10, blank=False)
    size = models.IntegerField(default = 1, blank = False)
    # val = (getData.CPUData())
    # val2 = (getData.CPUCoolerData())
    # val3 = (getData.GPUData())
    # image_url = models.ImageField(upload_to=upload_to, blank=True, null=True, default=val)
    # image_url2 = models.ImageField(upload_to=upload_to, blank=True, null=True, default=val2)
    # image_url3 = models.ImageField(upload_to=upload_to, blank=True, null=True, default=val3)  
    def lastUser(self):
        UserData.objects.get().last()

class OutputComputer(models.Model):
    cpu = models.CharField(max_length=50, default="nothing")
    cpu_p = models.FloatField(blank =False, default = 10)
    gpu = models.CharField(max_length=50, default="nothing")
    gpu_p = models.FloatField(blank =False, default = 10)
    cpuCooler = models.CharField(max_length=50, default="nothing")
    cpuCooler_p = models.FloatField(blank =False, default = 10)
    motherboard = models.CharField(max_length=50, default="nothing")
    motherboard_p = models.FloatField(blank =False, default = 10)
    storage = models.CharField(max_length=50, default="nothing")
    storage_p = models.FloatField(blank =False, default = 10)
    memory = models.CharField(max_length=50, default="nothing")
    memory_p = models.FloatField(blank =False, default = 10)
    total_price = models.FloatField(max_length=50, default = 10)
    case = models.CharField(max_length=50, default="nothing")
    case_p = models.FloatField(blank =False, default = 10)
    powerSupply = models.CharField(max_length=50, default="nothing")
    powerSupply_p = models.FloatField(blank =False, default = 10)


class AllData(models.Model): # All data compiled here
    DEFAULT_PK = 1
    num = models.IntegerField(default = DEFAULT_PK)

    def __str__(self):
        return "All Data"

class Motherboard(models.Model):
    price = models.FloatField(blank = False, default=10)
    name = models.CharField(blank = False, default = "", max_length=50)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="motherboard")
    size = models.CharField(blank = False, default = "", max_length=50)

    def __str__(self):
        return self.name

class CPU(models.Model):
    price = models.FloatField(blank=False)
    coreCount = models.FloatField(blank=True)
    clockSpeed = models.FloatField(blank=True)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="CPU")
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name

class CPUCooler(models.Model):
    price  = models.FloatField(blank=False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="CPUCooler")
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name
    
class Memory(models.Model):
    price = models.FloatField()
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="memory")
    name = models.TextField(blank=True, max_length=50)
    gigs = models.IntegerField(blank = False, default = 0, null=True)

    def __str__(self):
        return self.name   
    
class Storage(models.Model):
    ssd = models.BooleanField(default = False)
    price = models.FloatField(blank = False)
    capacity = models.FloatField(blank = False, default=0)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name='storage')
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name   
    
class GPU(models.Model):
    price = models.FloatField(blank = False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name='GPU')
    name = models.TextField(blank=True, max_length=50)
    coreClock = models.IntegerField(blank = True, default = 0)
    memory = models.IntegerField(blank=True, default = 0)
    def __str__(self):
        return self.name  

class Case(models.Model):
    price = models.FloatField(default = 0, blank = False)
    size = models.CharField(default="unknown", blank=False, max_length=60)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name='case')
    name = models.TextField(blank= False , max_length=50)
    color = models.CharField(default="unknown", blank=False, max_length=30)
    
    def __str__(self):
        return self.name  


class PowerSupply(models.Model):
    price = models.FloatField(blank = False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="powerSupply")
    name = models.TextField(blank=True, max_length=50,)
    watts = models.IntegerField(blank=False, default=0)
    effiency = models.CharField(max_length=50, blank=False, default="")
    def __str__(self):
        return self.name
    
