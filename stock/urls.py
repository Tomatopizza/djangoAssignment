from django.urls import path, include
from . import views

urlpatterns = [
    path('inbound/', views.inbound, name='inbound'),
]