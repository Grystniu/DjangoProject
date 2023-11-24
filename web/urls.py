from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('registration/', views.registartion_view, name='registration_view'),
]
