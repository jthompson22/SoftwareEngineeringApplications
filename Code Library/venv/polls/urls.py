from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #path('post-quantity-data/', views.post_quantity_data, name='qauntitydata')
]
