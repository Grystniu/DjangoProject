from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

from web.forms import RegistrationForm, AuthForm, RoomForm
from .models import Room

# Create your views here.

User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, 'web/main.html', {
        'year': year,
    })


def registartion_view(request):
    form = RegistrationForm()
    is_succses = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(form.cleaned_data)
            is_succses = True
    return render(request, "web/registration.html",
                  {'form': form, 'is_succses': is_succses,
                   })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Пользователь не найден")
            else:
                login(request, user)
                return redirect('main')

    return render(request, 'web/auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            form.save_m2m()
            # Перенаправляем на страницу списка комнат
            return redirect('room_list')
    else:
        form = RoomForm()

    return render(request, 'create_room.html', {'form': form})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})
