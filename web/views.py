from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import get_user_model

from web.forms import RegistrationForm

# Create your views here.

User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, 'web/index.html', {
        'year': year,
    })


def registartion_view(request):
    form = RegistrationForm()
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
    return render(request, "web/registration.html", {'form': form, })
