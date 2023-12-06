from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('list_users/', views.list_users, name='users-list_users'),
    path('get_user_profile/<int:id>/', views.get_user_profile, name='users-get_user_profile'),
]

