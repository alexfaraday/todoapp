from django import forms
from .models import *



class addnewtask(forms.ModelForm):
    class Meta:
        model=hometasks
        fields=['taskname', ]
        required_fields = ['taskname']
        widgets = {'taskname': forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
                #  'taskenddate': forms.DateTimeInput(attrs={'class': 'form-control', 'required':'required'}),





                   }