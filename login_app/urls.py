from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateUser, name='create_user'),
    path('auth/', views.AuthUser, name='auth_user'),
]