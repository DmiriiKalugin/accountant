from django import forms
from .models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = (
            'name',
            'price',
        )
        widgets = {
            'price': forms.TextInput,
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'number',
            'email',
        )
        widgets = {
            'name': forms.TextInput,
        }


class SendForm(forms.Form):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    number = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Номер телефона', 'class': 'form-control'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Сообщение', 'class': 'form-control'}), required=True)
