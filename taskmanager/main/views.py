from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import *
from PIL import Image
from .models import *
from .forms import *
import time


image_folder = 'main/images/'
anon_image_name = 'anon.jpg'


def home(request):
    return render(request, 'main/home.html')


# ========================= Chat manager ================================

def getChat(request):
    if 'chat_name' in request.GET:
        chat = Chat.objects.get(name=request.GET['chat_name'])
    else:
        chat = Chat.objects.get(id=request.GET['chat_id'])

    messages = Message.objects.filter(chat=chat)

    context = {
        'chat': chat,
        'messages': messages
    }

    return render(request, 'main/chat.html', context)


# ======================= Employee manager ==============================

def getEmployees(request):
    employees = Employee.objects.order_by('id')

    return render(request, 'main/employees/getEmployees.html', {
        'title': 'Employees',
        'employees': employees
    })


def addEmployee(request):
    error = ''

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            full_name = anon_image_name

            if 'file' in request.FILES:
                image_name = str(request.FILES['file'].name).replace(' ', '')
                employee_name = str(form.data['name']).replace(' ', '')
                full_name = employee_name + str(int(time.time())) + image_name

                with Image.open(request.FILES['file'], 'r') as im:
                    im.convert('RGB').save(f'{image_folder + full_name}')

            form.save()

            #last_employee = Employee.objects.latest('id')
            #last_employee.imagePath = image_folder + full_name
            #last_employee.save()

            return redirect('getEmployees')
        else:
            error = "There is some error"

    form = EmployeeForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/employees/addEmployee.html', context)


def infoEmployee(request):
    employee = Employee.objects.get(id=request.GET['employee_id'])
    context = {'employee': employee}

    return render(request, 'main/employees/infoEmployee.html', context)


def editEmployee(request):
    error = ''

    employee = Employee.objects.get(id=request.GET['employee_id'])

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('getEmployees')
        else:
            error = "There is some error"

    form = EmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'form': form,
        'error': error
    }

    return render(request, 'main/employees/editEmployee.html', context)


def dellEmployeeSure(request):
    employee = Employee.objects.get(id=request.GET['employee_id'])
    context = {'employee': employee}

    return render(request, 'main/employees/dellEmployee.html', context)


def dellEmployee(request):
    Employee.objects.get(id=request.GET['employee_id']).delete()
    return redirect('getEmployees')


# ========================= Task manager ================================

def getTasks(request):
    tasks = Task.objects.order_by('id')

    return render(request, 'main/tasks/getTasks.html', {
        'title': 'Tasks',
        'tasks': tasks
    })


def addTask(request):
    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            chat = Chat(name=form.data['name'])
            form.Meta.model.chat = chat

            chat.save()
            form.save()
            return redirect('getTasks')
        else:
            error = "There is some error"

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/tasks/addTask.html', context)


def infoTask(request):
    task = Task.objects.get(id=request.GET['task_id'])
    context = {'task': task}

    return render(request, 'main/tasks/infoTask.html', context)


def editTask(request):
    error = ''

    task = Task.objects.get(id=request.GET['task_id'])

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('getTasks')
        else:
            error = "There is some error"

    form = TaskForm(instance=task)

    context = {
        'task': task,
        'form': form,
        'error': error
    }

    return render(request, 'main/tasks/editTask.html', context)


def dellTaskSure(request):
    task = Task.objects.get(id=request.GET['task_id'])
    context = {'task': task}

    return render(request, 'main/tasks/dellTask.html', context)


def dellTask(request):
    task = Task.objects.get(id=request.GET['task_id'])
    if task.chat is not None:
        task.chat.delete()
    task.delete()

    return redirect('getTasks')


# ========================= Role manager ================================

def getRoles(request):
    roles = Role.objects.order_by('id')

    return render(request, 'main/roles/getRoles.html', {
        'title': 'Roles',
        'roles': roles
    })


def addRole(request):
    error = ''

    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getRoles')
        else:
            error = "There is some error"

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

    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('getRoles')
        else:
            error = "There is some error"

    form = RoleForm(instance=role)

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
    Role.objects.get(id=request.GET['role_id']).delete()
    return redirect('getRoles')
