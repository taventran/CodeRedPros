from django.contrib import admin
from web.models import CPU, AllData, CPUCooler, GPU

# Register your models here.
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(CPUCooler)
admin.site.register(AllData)
