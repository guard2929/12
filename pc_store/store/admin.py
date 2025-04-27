from django.contrib import admin
from .models import  CPU, GPU, RAM, Storage, PCBuild, Product

admin.site.register(Product)
admin.site.register(PCBuild)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Storage)