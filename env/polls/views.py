from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import WaterQuantity, WaterQuality


#admin.site.register(WaterQuality)
#admin.site.register(WaterQuantity)

def home(request):
    if request.method == 'POST':
        if 'water_quality' in request.POST:
            form = WaterQuantity(request.POST or None)
        elif 'water_quantity' in request.POST:
            form = WaterQuality(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
    return render(request, 'home.html', {})


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
    




