from django.shortcuts import render
from django.http import HttpResponse
from .models import MainModel
from .forms import MainModelForm

def index(request):
    main_models = MainModel.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'main_models': main_models})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    form = MainModelForm()
    if request.method == 'POST':
        form = MainModelForm(request.POST, request.FILES)
        if form.is_valid():
            task = MainModel(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
            )
            task.save()
    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context)
