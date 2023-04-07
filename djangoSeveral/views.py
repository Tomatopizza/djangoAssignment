from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        return render(request, 'home.html')