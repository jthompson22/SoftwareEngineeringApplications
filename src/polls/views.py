from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import WaterQuality
import json
from .models import WaterQualityData


#admin.site.register(WaterQuality)
#admin.site.register(WaterQuantity)

def home(request):

    if request.method == 'POST':
        form = WaterQuality(request.POST or None)
        if form.is_valid():
            print(form.data)
            water_quality_dict={
                'Collection Date' : form.data['collection_date_month'] + '/' + form.data['collection_date_day'] + '/' + form.data['collection_date_year'],
                'Collection Time' : form.data['collection_time'],
                'Site ID' : form.data['site_id'],
                'Collector Initials' : form.data['collector_initials'],
                'Jar Number' : form.data['jar_number'],
                'Parameter' : form.data['parameter'],
                'Pval One' : form.data['pval_one'],
                'Pval Two' : form.data['pval_two'],
                'Pval Three' : form.data['pval_three'],
                'Average' : form.data['average'],
                'Analyst Intials' : form.data['analyst_initials'],
                'Enterer Initials' : form.data['enterer_intials'],
                'Notes' : form.data['notes']
            } 
            
            #water_quality_dict = json.loads(water_quality_dict)
            print(water_quality_dict)
            data_object = WaterQualityData(collection_data=water_quality_dict)
            data_object.save()

            form = WaterQuality(request.POST or None)
            return render(request, 'home.html', {"forms": form})
    else:
        form = WaterQuality(request.POST or None)
        return render(request, 'home.html', {"forms": form})


def water_quality(request):
    if request.method == 'POST':
        form = WaterQuality(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})

def water_quantity(request):
    return render(request, 'water_quantity.html', {})
    




