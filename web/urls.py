from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('registration/', views.registartion_view, name='registration'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('create_room/', views.create_room, name='create_room'),
    path('room_list/', views.room_list, name='room_list'),
]
