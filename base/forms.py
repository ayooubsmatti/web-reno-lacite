from django.forms import ModelForm
from django import forms
from .models import DemendeUnAppel
from django.db import models

class DemendeUnAppelForm(ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    name.widget.attrs.update({'class': 'form-control  border-0 '})
    name.widget.attrs.update({'style' : 'height: 55px;'})
    email =forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Email ...'}))
    email.widget.attrs.update({'class': 'form-control border-0 '})
    email.widget.attrs.update({'style' : 'height: 55px;'})
    date = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your username  date'}))
    date.widget.attrs.update({'class': 'form-control border-0 datetimepicker-input'})
    date.widget.attrs.update({'style' : 'height: 55px;'})
    date.widget.attrs.update({'data-target' : "#date" })
    date.widget.attrs.update({'data-toggle' : "datetimepicker"})
    time = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Call Back Date'}))
    time.widget.attrs.update({'class': 'form-control border-0 datetimepicker-input'})
    time.widget.attrs.update({'style' : 'height: 55px;'})
    time.widget.attrs.update({'data-target' : "#time" })
    time.widget.attrs.update({'data-toggle' : "datetimepicker"})
    message = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={'placeholder': 'Message ...'}))
    message.widget.attrs.update({'class': 'form-control border-0 '})
    message.widget.attrs.update({'style' : 'height: 55px;'})
    message.widget.attrs.update({'rows' : "5"})
    
    class Meta:
        model = DemendeUnAppel
        fields = '__all__'