from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import WaterQuantity, WaterQuality


#admin.site.register(WaterQuality)
#admin.site.register(WaterQuantity)

def index(request):
    if request.method == 'POST':
        form = WaterQuantity(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})


#def post_quantity_data(request):
    




