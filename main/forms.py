from .models import MainModel
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class MainModelForm(ModelForm):
    class Meta:
        model = MainModel
        fields = ['title', 'description', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введиет описание задачи'
            }),
        }

    # title = forms.CharField(
    #     max_length=50,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите название задачи'
    #     })
    # )
    # description = forms.CharField(
    #     widget=forms.Textarea(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введиет описание задачи'
    #     })
    # )



