from datetime import datetime

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from .forms.forms import *
from .models import *

from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.household_set.all().count() != 0:
            uuid = str(request.user.profile.household_set.all()[0].household_id)
            url = '/' + uuid
            return redirect(url)
        else:
            return redirect('joinGroup')
    return redirect('login')


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
                request.user.profile.household_set.all()[0].bulletins.add(bulletin)
                return redirect('dashboard')
    form = BulletinForm()
    return render(request, 'users/bulletin.html', {'form': form})


def create_household(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HouseholdCreateForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['household_name']
                pin = form.cleaned_data['household_pin']
                household = Household.objects.create(name=name,
                                                    pin = pin)
                return redirect('/')
    form = HouseholdCreateForm()
    return render(request, 'users/createHousehold.html', {'form': form})

def join_household(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = JoinGroupForm(request.POST)
            profile = Profile.objects.get(user = request.user)
            if form.is_valid():
                enteredPin = form.cleaned_data['household_pin']
                group = Household.objects.get(pin = enteredPin)
                group.profiles.add(profile)
                return redirect('/')
    form = JoinGroupForm()
    return render(request, 'users/joinHousehold.html', {'form': form})


def dashboard(request, household_id):
    if request.user.is_authenticated:
        household = get_object_or_404(Household, pk=household_id)
        chores = household.chores.all()
        user_name = request.user.username
        total_points = None
        new_tasks = None
        completed_tasks = None
        points_earned_today = None
        unclaimed_tasks = chores.filter(claimed=False)
        unclaimed_tasks_count = unclaimed_tasks.count()
        unclaimed_points = unclaimed_tasks.aggregate(Sum('points'))['points__sum']
        if unclaimed_points == None:
            unclaimed_points = 0
        bulletins = household.bulletins.all()
        values = {'user_name': user_name,
                 'total_points': total_points,
                 'new_tasks': new_tasks,
                 'completed_tasks': completed_tasks,
                 'points_earned_today': points_earned_today,
                 'unclaimed_tasks_count': unclaimed_tasks_count,
                 'unclaimed_points': unclaimed_points,
                 'bulletins': bulletins,}
        return render(request, 'users/dashboard.html', values) 
