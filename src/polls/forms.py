#from .models import WaterQualityData
from django import forms
from .rivernet_api import Get_Site_Information
import datetime

class WaterQuality(forms.Form):
    site_dictionary = Get_Site_Information()

    PARAMETER_CHOICES=[
        ('Nitrate', 'Nitrate'),
        ('Orthophosphate', 'Orthophosphate'),
        ('pH', 'pH'),
        ('Temperature', 'Temperature'),
        ('Total Nitrogen', 'Total Nitrogen'),
        ('Nitrite', 'Nitrite'),
        ('Total Phosphorous', 'Total Phosphorous'),
    ]


    SITE_ID_CHOICES = []
    for items in site_dictionary:
        our_tuple = (items["id"], items["sitename"])
        SITE_ID_CHOICES.append(our_tuple)

    print(SITE_ID_CHOICES)
    INTEGER_CHOICES = [tuple([x,x]) for x in range(1,51)]
    print(INTEGER_CHOICES)

    collection_date = forms.DateTimeField(label="Collection Date:", widget= forms.SelectDateWidget) 
    collection_time = forms.TimeField(label="Collection Time:", widget=forms.TimeInput, initial= datetime.datetime.now().time())

    site_id = forms.CharField(label="Site ID:", widget=forms.Select(choices=SITE_ID_CHOICES))

    collector_initials = forms.CharField(max_length=3) 

    jar_number = forms.IntegerField(label="Jar Number:", widget=forms.Select(choices=INTEGER_CHOICES))

    parameter = forms.CharField(label="Parameter:", widget=forms.Select(choices=PARAMETER_CHOICES))

    #__________

    pval_one = forms.FloatField(label="Pval One:", widget=forms.NumberInput(attrs={'step': '.1'})) #do we want these to have a bound?
    pval_two = forms.FloatField(label="Pval Two:", widget=forms.NumberInput(attrs={'step': '.1'}))
    pval_three = forms.FloatField(label="Pval Three:", widget=forms.NumberInput(attrs={'step': '.1'}))
    average = forms.FloatField(label="Average:", widget=forms.NumberInput(attrs={'step': '.1'}))

    analyst_initials = forms.CharField(max_length=3, label="Analyst Initials:")
    enterer_intials = forms.CharField(max_length=3, label="Enterer Initials:")
    notes = forms.CharField(max_length=500, label="Notes:")




    


