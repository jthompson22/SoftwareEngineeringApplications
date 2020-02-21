from .models import WaterQuality, WaterQuantity
from django import forms

class WaterQuality(forms.ModelForm):
    class Meta:
        model = WaterQuality
        fields = ['site_id', 'parameter', 'jar_number', 'collection_time', 'pval_one', 'pval_two', 'pval_three', 'collector_initials', 'analyst_initials', 'enterer_intials', 'notes']


class WaterQuantity(forms.ModelForm):
    class Meta:
        model = WaterQuantity
        fields = ['date', 'pressure_difference', 'pressure_absolute', 'temperature', 'water_level', 'pressure_baro', 'reference_water_level', 'water_density']

