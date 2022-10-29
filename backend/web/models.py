from django.db import models


# Create your models here.

class OutputComputer(models.Model):
     # Make serializer for this. 
     # will be finalized suggestion
    total_price = models.FloatField(blank = False)

class AllData(models.Model): # All data compiled here
    DEFAULT_PK = 1
    num = models.IntegerField(default = DEFAULT_PK)

    def __str__(self):
        return "All Data"

class CPU(models.Model):
    price = models.FloatField(blank=False)
    coreCount = models.FloatField(blank=True)
    performanceCoreClock = models.FloatField(blank=True)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="CPU")
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name

class CPUCooler(models.Model):
    price  = models.FloatField(blank=False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE)
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name
    



class Memory(models.Model):
    price = models.FloatField()
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE, related_name="memory")
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name   
    


class Storage(models.Model):
    ssd = models.BooleanField(default = False)
    hardDrives = models.BooleanField(default = False)
    price = models.FloatField(blank = False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE)
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name   
    



class GPU(models.Model):
    price = models.FloatField(blank = False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE)
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name  
    


class PowerSupply(models.Model):
    price = models.FloatField(blank = False)
    allData = models.ForeignKey(AllData, default = AllData.DEFAULT_PK, on_delete=models.CASCADE)
    name = models.TextField(blank=True, max_length=50)
    
    def __str__(self):
        return self.name
    

