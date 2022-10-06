from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Chat', views.chat, name='chat'),
    path('Employees', views.employees, name='employees'),
    path('Roles', views.getRoles, name='getRoles'),
    path('addRole', views.addRole, name='addRole'),
    path('infoRole', views.infoRole, name='infoRole'),
    path('editRole', views.editRole, name='editRole'),
    path('dellRoleSure', views.dellRoleSure, name='dellRoleSure'),
    path('dellRole', views.dellRole, name='dellRole'),
    path('Tasks', views.tasks, name='tasks'),

]
