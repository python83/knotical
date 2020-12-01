from django.urls import path
from . import views

app_name = 'taskmanager'

urlpatterns = [
    path('tasks', views.tasks_index, name='tasks_index'),
    path('tasks/topics', views.topics_index, name='topics'),
    path('tasks/add', views.tasks_add, name='tasks_add'),
    path('tasks/edit/<str:title>', views.tasks_edit, name='tasks_edit'),
]
