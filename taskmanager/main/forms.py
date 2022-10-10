from .models import *
from django.forms import ModelForm, Form, TextInput, Textarea, SelectMultiple, NumberInput
from django.forms import EmailInput, ClearableFileInput, FileField, FileInput, FilePathField, ImageField
from django.core.files import File


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


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'login', 'password', 'age', 'email', 'phone', 'role']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Login'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'age': NumberInput(attrs={'min': '0'}),
            'email': EmailInput(),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            'role': SelectMultiple(choices=Role.objects.all())
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




