from django.contrib import admin
from web.models import CPU, AllData, CPUCooler, GPU, Memory, Storage, PowerSupply, Case

# Register your models here.
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(CPUCooler)
admin.site.register(Memory)
admin.site.register(Storage)
admin.site.register(PowerSupply)
admin.site.register(Case)
admin.site.register(AllData)
