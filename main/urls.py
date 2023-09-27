from django.urls import path

from main import views

urlpatterns = [
    path("", views.tasks_list, name="home"),
    path("add_task", views.add_task, name="add_task"),
    path("edit_task/<int:pk>", views.edit_task, name="edit_task"),
    path("delete_task/<int:pk>", views.delete_task, name="delete_task"),
    path("task_status/<int:pk>", views.task_status, name="task_status"),
]
