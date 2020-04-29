#from .models import WaterQualityData
from django import forms
from .rivernet_api import Get_Site_Information
import datetime
from django.forms import formset_factory
from django.forms import BaseFormSet


class WaterQualityHeader(forms.Form):
    PARAMETER_CHOICES=[
        ('Nitrate', 'Nitrate'),
        ('Orthophosphate', 'Orthophosphate'),
        ('pH', 'pH'),
        ('Temperature', 'Temperature'),
        ('Total Nitrogen', 'Total Nitrogen'),
        ('Nitrite', 'Nitrite'),
        ('Total Phosphorous', 'Total Phosphorous'),
    ]
    INTEGER_CHOICES = [tuple([x,x]) for x in range(1,51)]
    collection_date = forms.DateTimeField(label="Collection Date:", widget= forms.SelectDateWidget) 
    collection_time = forms.TimeField(label="Collection Time:", widget=forms.TimeInput, initial= datetime.datetime.now().time())
    parameter = forms.CharField(label="Parameter:", widget=forms.Select(choices=PARAMETER_CHOICES))

    collector_initials = forms.CharField(max_length=3)
    enterer_intials = forms.CharField(max_length=3, label="Enterer Initials:")
    #_________
    
    collected_amount = forms.IntegerField(label="Number of Data Values to Enter:", widget=forms.Select(choices=INTEGER_CHOICES))





class WaterQuality(forms.Form):
    site_dictionary = Get_Site_Information()
    '''PARAMETER_CHOICES=[
        ('Nitrate', 'Nitrate'),
        ('Orthophosphate', 'Orthophosphate'),
        ('pH', 'pH'),
        ('Temperature', 'Temperature'),
        ('Total Nitrogen', 'Total Nitrogen'),
        ('Nitrite', 'Nitrite'),
        ('Total Phosphorous', 'Total Phosphorous'),
    ]'''
    SITE_ID_CHOICES = []
    for items in site_dictionary:
        our_tuple = (items["id"], items["id"])
        SITE_ID_CHOICES.append(our_tuple)

    print(SITE_ID_CHOICES)
    INTEGER_CHOICES = [tuple([x,x]) for x in range(1,51)]
    print(INTEGER_CHOICES)

    #collection_date = forms.DateTimeField(label="Collection Date:", widget= forms.SelectDateWidget) 
    #collection_time = forms.TimeField(label="Collection Time:", widget=forms.TimeInput, initial= datetime.datetime.now().time())

    site_id = forms.CharField(label="Site ID:", widget=forms.Select(choices=SITE_ID_CHOICES))

    #collector_initials = forms.CharField(max_length=3) 

    jar_number = forms.IntegerField(label="Jar Number:", widget=forms.Select(choices=INTEGER_CHOICES))

    #parameter = forms.CharField(label="Parameter:", widget=forms.Select(choices=PARAMETER_CHOICES))

    #__________
    pval_one = forms.FloatField(label="P1:", widget=forms.NumberInput(attrs={'step': '.1'}), min_value=0) #do we want these to have a bound?
    pval_two = forms.FloatField(label="P2:", widget=forms.NumberInput(attrs={'step': '.1'}), min_value=0)
    pval_three = forms.FloatField(label="P3:", widget=forms.NumberInput(attrs={'step': '.1'}),min_value=0)
    #average = forms.FloatField(label="Average:", widget=forms.NumberInput(attrs={'step': '.1'}))

    analyst_initials = forms.CharField(max_length=3, label="Analyst Initials:")
    #enterer_intials = forms.CharField(max_length=3, label="Enterer Initials:")
    notes = forms.CharField(max_length=500, label="Notes:", required=False)


class Base_Formset(BaseFormSet):
    def clean(self):
        site_id_list = []
        jar_id_list = []

        if any(self.errors):
            #self.append_non_form_error("The dataset contains a noninque jar number and site ID. Change this and try again.")
            return
            raise forms.ValidationError("The dataset contains a noninque jar number and site ID. Change this and try again.")      

        site_id_list = []
        jar_id_list = []
        for form in self.forms:
            site_id = form.cleaned_data.get('site_id')
            jar_number = form.cleaned_data.get('jar_number')
                #site_id_list.append(form['site_id'])
                #jar_id_list.append(form['jar_number'])
            if site_id in site_id_list:
                raise forms.ValidationError("One of the Site ID's is repeated. Check the dataset.") 
            if jar_number in jar_id_list:
                raise forms.ValidationError("One of the Jar numbers is repeated. Check the dataset.")
            site_id_list.append(site_id)
            jar_id_list.append(jar_number)
        
        #if len(site_id_list) != len(set(site_id_list)) and len(jar_id_list) != len(set(jar_id_list)):
            #self.append_non_form_error("The dataset contains a noninque jar number and site ID. Change this and try again.")
        #    raise forms.ValidationError("The dataset contains a noninque jar number and site ID. Change this and try again.")      
        #if len(site_id_list) != len(set(site_id_list)):
            #self.append_non_form_error("One of the Site ID's is repeated. Check the dataset.")
        #    raise forms.ValidationError("One of the Site ID's is repeated. Check the dataset.") 
        #if len(jar_id_list) != len(set(jar_id_list)):
            #self.append_non_form_error("One of the Jar numbers is repeated. Check the dataset.")
        #    raise forms.ValidationError("One of the Jar numbers is repeated. Check the dataset.") 
        


#WaterQualityFormset = formset_factory(WaterQuality, extra=int(header.data['collected_amount']))





    


