from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('getChat', views.getChat, name='getChat'),

    path('getEmployees', views.getEmployees, name='getEmployees'),
    path('addEmployee', views.addEmployee, name='addEmployee'),
    path('infoEmployee', views.infoEmployee, name='infoEmployee'),
    path('editEmployee', views.editEmployee, name='editEmployee'),
    path('dellEmployeeSure', views.dellEmployeeSure, name='dellEmployeeSure'),
    path('dellEmployee', views.dellEmployee, name='dellEmployee'),

    path('Roles', views.getRoles, name='getRoles'),
    path('addRole', views.addRole, name='addRole'),
    path('infoRole', views.infoRole, name='infoRole'),
    path('editRole', views.editRole, name='editRole'),
    path('dellRoleSure', views.dellRoleSure, name='dellRoleSure'),
    path('dellRole', views.dellRole, name='dellRole'),

    path('Tasks', views.getTasks, name='getTasks'),
    path('addTask', views.addTask, name='addTask'),
    path('infoTask', views.infoTask, name='infoTask'),
    path('editTask', views.editTask, name='editTask'),
    path('dellTaskSure', views.dellTaskSure, name='dellTaskSure'),
    path('dellTask', views.dellTask, name='dellTask'),

]
