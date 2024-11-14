from django.urls import path
from . import views

urlpatterns =[
    path("addTask/", views.addTask, name="add_task"),
    path("",views.taskList,name='task_list'),
    path("diplayTL/",views.task_list,name="displayTL")
]

