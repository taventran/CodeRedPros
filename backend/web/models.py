from django.db import models
from numpy import maximum


# Create your models here.

class UserData(models.Model):
    use = models.IntegerField(default = 1, blank = False)
    aesthetic = models.BooleanField(default=False)
    priceRange = models.FloatField(default=10, blank=False)
    size = models.IntegerField(default = 1, blank = False)

class OutputComputer(models.Model):
     # Make serializer for this. 
     # will be finalized suggestion
    total_price = models.FloatField(blank = False)

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
    gigs = models.IntegerField(blank = False, default = 0)

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
    
