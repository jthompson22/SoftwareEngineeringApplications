from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('water_quality/', views.water_quality, name='waterquality'),
    path('water_quantity/', views.water_quantity, name='waterquantity'),
    #path('admin/', admin.site.urls, name='admin'),
    #path('post-quantity-data/', views.post_quantity_data, name='qauntitydata')
]
