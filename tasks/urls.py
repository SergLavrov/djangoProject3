from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='tasks-register'),
    path('list_tasks/', views.list_tasks, name='tasks-list_tasks'),
    path('get_task_profile/<int:id>/', views.get_task_profile, name='tasks-get_task_profile'),
]
