from django import forms
from .models import Employees_detail
from django.forms import widgets

class Add_Employee_form(forms.ModelForm):
    class Meta:
        model = Employees_detail
        fields = ['name', 'email_id', 'phone_no', 'designation', 'image']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email_id' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
            'designation' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.ClearableFileInput(attrs={
                'class':'form-control',
                'accept': 'image/*',
                'style': 'border: 2px solid #ccc; padding: 10px;',
                }),
        }
