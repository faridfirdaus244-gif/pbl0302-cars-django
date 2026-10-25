from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carname', 'carbrand', 'carmodel', 'carprice']
        labels = {
            'carname': 'Name',
            'carbrand': 'Brand',
            'carmodel': 'Model',
            'carprice': 'Price',
        }
        widgets = {
            'carname': forms.TextInput(attrs={'class': 'form-control'}),
            'carbrand': forms.TextInput(attrs={'class': 'form-control'}),
            'carmodel': forms.TextInput(attrs={'class': 'form-control'}),
            'carprice': forms.TextInput(attrs={'class': 'form-control'}),
        }