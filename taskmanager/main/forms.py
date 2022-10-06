from .models import *
from django.forms import ModelForm, TextInput, Textarea


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            })
        }




