from django.contrib import admin
from .models import WaterQuantity

# Register your models here.

@admin.register(WaterQuantity)

class WaterQuantityAdmin(admin.ModelAdmin):
    list_display = ['river_name', 'enteree']