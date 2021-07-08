from django import forms
from django.forms import fields, widgets
from .models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form__input'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form__input'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почта', 'class': 'form__input'}),
            'number': forms.TextInput(attrs={'placeholder': 'Номер телефона', 'class': 'form__input'}),
        }


class AddRequest(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'surname', 'number', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form__input'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form__input'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почта', 'class': 'form__input'}),
            'number': forms.TextInput(attrs={'placeholder': 'Номер телефона', 'class': 'form__input'}),
            'text': forms.Textarea(attrs={'placeholder': 'Номер телефона', 'class': 'form__input'}),
        }