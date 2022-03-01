from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.LoginPage, name='LoginPage'),
    path('register/', views.RegisterPage, name='RegisterPage'),

]
