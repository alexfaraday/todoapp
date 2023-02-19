from django import forms

from .models import *


class addnewtask(forms.ModelForm):
    class Meta:
        model = hometasks
        fields = ["taskname", "taskdescription"]
        required_fields = ["taskname"]
        widgets = {
            "taskname": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "taskdescription": forms.Textarea(
                attrs={"class": "form-control", "required": "required"}
            ),
        }
