from django.db import models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

'''
def generate_graph():
    cpu_name = ["AMD 5600X", "AMD 5800X", "Intel Core i7", "AMD 5600", "Intel Core i5", "AMD 5900X"]
    cpu_price = [158.98, 249.00, 364.99, 139.99, 269.99, 349.99,]
    cpu_core_clock = [3.7, 3.8, 3.6, 3.5, 3.7, 3.7]

    sns.set_style("dark")
    data_plot_cpu1 = pd.DataFrame({"Name": cpu_name, "Price": cpu_price})
    data_plot_cpu2 = pd.DataFrame({"Name": cpu_name, "Core Clock": cpu_core_clock})
    sns.lineplot(x="Name", y="Price", data=data_plot_cpu1)
    sns.lineplot(x="Name", y="Core Clock", data=data_plot_cpu2)
    line = ""
    for i in range(10):
        line += str(random.randint(0, 9))
    
    line += ".png"
    plt.savefig(f"images/{line}")

    return f"images/{line}"

'''
# Create your models here.

def upload_to(instance, filename):
    return f'images/{filename}'

class UserData(models.Model):
    use = models.IntegerField(default = 1, blank = False)
    aesthetic = models.BooleanField(default=False)
    priceRange = models.FloatField(default=10, blank=False)
    size = models.IntegerField(default = 1, blank = False)
    #image_url = models.ImageField(upload_to=upload_to, blank=True, null=True, default=val)

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
    
