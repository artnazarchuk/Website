from django.shortcuts import render
from django.http import HttpResponse
from .models import Main_model

def index(request):
    main_models = Main_model.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'main_models': main_models})

def about(request):
    return render(request, 'main/about.html')

