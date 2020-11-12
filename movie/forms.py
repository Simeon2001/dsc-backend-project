from django import forms
from django.forms import ModelForm
from .models import toplist

class moviecreate (forms.ModelForm) :
    
    class Meta :
        model = toplist
        fields=('movie_name','genre','pics_url','year',)