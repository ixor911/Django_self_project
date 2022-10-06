from .models import *
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple


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


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'employees', 'chat']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'employees': SelectMultiple(choices=Employee.objects.all())
        }




