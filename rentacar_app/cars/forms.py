from django import forms
from django.forms import ModelForm
from .models import Cars


class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"

        widgets = {
            'mark' : forms.TextInput(attrs={'class':'form-control'}),
            'model' : forms.TextInput(attrs={'class':'form-control'}),
            'color' : forms.TextInput(attrs={'class':'form-control'}),
            'note' : forms.TextInput(attrs={'class':'form-control'}),
            }