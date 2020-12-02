from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task', views.get_task, name='getTask'),
    path('create', views.create_task, name='createTask'),
    path('delete', views.delete_task, name='deleteTask'),
    path('tasks', views.get_all_tasks, name='getAllTasks'),
    path('deleteAll', views.delete_all_tasks, name='deleteAllTasks')
]
