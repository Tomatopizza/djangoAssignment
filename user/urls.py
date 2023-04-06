from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
]