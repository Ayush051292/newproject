from django import forms
from django.forms import ModelForm
from .models import Djform

class DjformForm(ModelForm):
    class Meta:
        model=Djform
        fields="__all__"
        labels={'name':'Enter Name:', 'age':'Enter Age:'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
                 'age':forms.NumberInput(attrs={'class':'form-control','id':'age'}),
                 'email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
                 'website':forms.URLInput(attrs={'class':'form-control','id':'website'}),
                 'text_area':forms.Textarea(attrs={'id':'text_area'}),
                 }
        exclude={'word_count','created_at','updated_at',}