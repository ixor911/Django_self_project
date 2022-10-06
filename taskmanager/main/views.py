from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

mainChatName = 'Main'


def home(request):
    context = {
        'mainChatName': mainChatName
    }
    return render(request, 'main/home.html', context=context)


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

def employees(request):
    return render(request, 'main/employees.html')


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
