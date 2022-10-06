from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, 'main/home.html')


def employees(request):
    return render(request, 'main/employees.html')


def chat(request):
    return render(request, 'main/chat.html')


def tasks(request):
    return render(request, 'main/tasks.html')


def getRoles(request):
    roles = Role.objects.order_by('id')

    return render(request, 'main/roles/getRoles.html', {
        'title': 'Roles',
        'roles': roles
    })


def addRole(request):
    error = ''

    form = RoleForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/roles/addRole.html', context)


def infoRole(request):
    role = Role.objects.get(id=request.GET['role_id'])
    context = {'role': role}

    return render(request, 'main/roles/infoRole.html', context)


def editRole(request):
    error = ''
    role = Role.objects.get(id=request.GET['role_id'])
    form = RoleForm({
        'name': role.name,
        'description': role.description
    })

    context = {
        'role': role,
        'form': form,
        'error': error
    }

    return render(request, 'main/roles/editRole.html', context)


def dellRoleSure(request):
    role = Role.objects.get(id=request.GET['role_id'])
    context = {'role': role}

    return render(request, 'main/roles/dellRole.html', context)


def dellRole(request):
    print(f"Типо удалилась роль {request.GET['role_id']}")
    return redirect('getRoles')

