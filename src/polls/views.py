from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import WaterQuality
import json
from .models import WaterQualityData
from .forms import WaterQualityHeader
#from .forms import WaterQualityFormset
from django.forms import formset_factory


#admin.site.register(WaterQuality)
#admin.site.register(WaterQuantity)

def home(request):
    if request.method == 'POST':
        header = WaterQualityHeader(request.POST or None)
        #content block 1 via wordd
        print(header.data['collected_amount'])
        print(type(header.data['collected_amount']))
        
        WaterQualityFormset = formset_factory(WaterQuality, extra=int(header.data['collected_amount']))
        formset = WaterQualityFormset()
        return render(request, 'home.html', {"forms": header, "formset": formset})
    else:
        header = WaterQualityHeader(request.POST or None)
        return render(request, 'home.html', {"forms": header})


def water_quality(request):
    if request.method == 'POST':
        header = WaterQualityHeader(request.POST or None)
        WaterQualityFormset = formset_factory(WaterQuality, extra=int(header.data['collected_amount']))
        formset = WaterQualityFormset(request.POST or None)
        water_quality_dict = {

                'Collection Date' : request.POST.get('collection_date_month') + '/' + request.POST.get('collection_date_day') + '/' + request.POST.get('collection_date_year'),
                'Collection Time' : request.POST.get('collection_time'),
                'Collector Initials' : request.POST.get('collector_initials'),
                'Parameter' : request.POST.get('parameter'),
                'Enterer Initials' : request.POST.get('enterer_intials'),
        }
#------------------------------------------------------------------------

        for i in range(0, int(request.POST.get('collected_amount'))):
                jar_number = 'form-'+str(i)+'-jar_number'
                pval1 = 'form-'+str(i)+'-pval_one'
                pval2 = 'form-'+str(i)+'-pval_two'
                pval3 = 'form-'+str(i)+'-pval_three'
                analyst_initials = 'form-'+str(i)+'-analyst_initials'
                notes = 'form-'+str(i)+'-notes'
                site_id = 'form-'+str(i)+'-site_id'
                site_id = request.POST.get(site_id)

                try:
                    var = [float(request.POST.get(pval1)), float(request.POST.get(pval2)), float(request.POST.get(pval3))]
                    average = round((sum(var))/(len(var)), 3)
                except ValueError:
                    average = ''
        

                data = {

                'Jar Number' : request.POST.get(jar_number),
                'Parameter Values' : [request.POST.get(pval1), request.POST.get(pval2),request.POST.get(pval3)],
                'Average' : average,
                'Analyst Intials' : request.POST.get(analyst_initials),
                'Notes' : request.POST.get(notes)
                }
                water_quality_dict[site_id] = data

        #water_quality_dict = json.loads(water_quality_dict)
        data_object = WaterQualityData(collection_data=water_quality_dict)
        data_object.save()
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})

def water_quantity(request):
    return render(request, 'water_quantity.html', {})
    




