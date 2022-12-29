from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def info(request):
    return HttpResponse('<a href="/">Новый текст, ссылка на главную</a>')

