from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms.forms import *
from .models import *


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created')
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def post_bulletin(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BulletinForm(request.POST)
            if form.is_valid():
                user = request.user.username
                bulletin_body = form.cleaned_data['bulletin_body']
                creation_time = datetime.now()
                expire_time = form.cleaned_data['expire_time']
                bulletin = Bulletin.objects.create(user=user,
                                                   bulletin_body=bulletin_body,
                                                   creation_time=creation_time,
                                                   expire_time=expire_time, )
                return redirect('/')
    form = BulletinForm()
    return render(request, 'users/bulletin.html', {'form': form})