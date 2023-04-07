from django.urls import path, include
from . import views

urlpatterns = [
    path('inbound/', views.inbound, name='inbound'),
    path('outbound/', views.outbound, name='outbound'),
    path('inventory/', views.inventory, name='inventory'),
]