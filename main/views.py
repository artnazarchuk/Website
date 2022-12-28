from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="info">Ссылка на новый текст</a>')

def info(request):
    return HttpResponse('<a href="/">Новый текст, ссылка на главную</a>')

