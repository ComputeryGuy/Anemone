import datetime
import calendar
import json
import random
import os
from pathlib import Path

from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.utils import timezone
from .forms.forms import *
from .models import *

from django.http import HttpResponse
from django.http import JsonResponse

import wonderwords
from wonderwords import RandomWord


from django.forms.models import model_to_dict

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.household is not None:
            return redirect('dashboard')
        else:
            return redirect('join')
    return redirect('login')


def login_reg(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("Oops")
        if request.POST.get('submit') == 'sign_up':
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            
            user = User.objects.create_user(username, password=password)
            if user is not None:
                profile = Profile.objects.get(user=user)
                profile.first_name = first_name
                profile.last_name = last_name
                profile.save()
                return redirect('login')
            else:
                print("OOPS")
                return redirect('login')

    user_creation_form = UserCreationForm()
    context = {'user_creation_form': user_creation_form}
    return render(request, 'users/log-in.html', context)


def join(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = Profile.objects.get(user=request.user)
            try: 
                payload = json.loads(request.body)
                household = Household.objects.create(pin=payload.get("house_pin"))
                profile.household = household
                profile.save()
                household.save()
            except:
                household_pin = request.POST.get('house_pin', '')
                try:
                    household = Household.objects.get(pin=household_pin)
                    profile.household = household
                    profile.save()
                    household.save()
                except:
                    pass
                return redirect('home')

        collides = True
        while collides:
            household_pin = random.randint(100000, 999999)
            if Household.objects.filter(pin=household_pin).count() == 0:
                collides = False
        return render(request, 'users/join.html', {'household_pin': household_pin})


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
                if form.cleaned_data['expire_date'].date() >= datetime.date.today():
                    bulletin = Bulletin(
                        user=request.user.username,
                        title=form.cleaned_data['title'],
                        bulletin_body=form.cleaned_data['bulletin_body'], 
                        expire_date=form.cleaned_data['expire_date'], 
                        household = request.user.profile.household)
                    bulletin.save()
                    return redirect('bulletin')
                else:
                    messages.error(request, "Failed: Expire date cannot be in the past")
                    return redirect('bulletin')
            else:
                messages.error(request, "Failed: Title or Detail should be filled out")
                return redirect('bulletin')
        else:
            form = BulletinForm()
            bulletins = Bulletin.objects.filter(household=request.user.profile.household)
            return render(request, 'users/bulletin.html', {
                'form': form,
                'bulletins': bulletins
            })


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


#alternative heading if url join implemented
#def join_household(request, household_id):
def join_household(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = JoinGroupForm(request.POST)
            profile = Profile.objects.get(user = request.user)
            ##possibly needed if url join implemented with above header
            ##household = Household.objects.get(household_id)
            if form.is_valid():
                enteredPin = form.cleaned_data['household_pin']
                group = Household.objects.get(pin = enteredPin)
                profile.household = group
                profile.save()
                return redirect('/')
    form = JoinGroupForm()
    return render(request, 'users/joinHousehold.html', {'form': form})

##need to edit above view/ to make this usable
####THIS WORKS
def generate_household_link(request):
    if request.user.is_authenticated:
        if request.user.profile.household is not None:
            uuid = str(request.user.profile.household.household_id)
            url = 'http://127.0.0.1:8000//joinHousehold/' + uuid
            print(url)
            return HttpResponse(url)
        
    


def dashboard(request):
    if request.user.is_authenticated:
        task_assign(request)
        household = request.user.profile.household
        tasks = household.task_set.all()
        user_name = request.user.username
        total_points = None
        new_tasks = None
        completed_tasks = None
        points_earned_today = None
        unclaimed_tasks = tasks.filter(claimed=False)
        unclaimed_tasks_count = unclaimed_tasks.count()
        unclaimed_points = unclaimed_tasks.aggregate(Sum('points'))['points__sum']
        unstarted_count = None
        in_progress_count = None
        if unclaimed_points == None:
            unclaimed_points = 0
        bulletins = household.bulletin_set.all()
        values = {'user_name': user_name,
                 'total_points': total_points,
                 'new_tasks': new_tasks,
                 'completed_tasks': completed_tasks,
                 'points_earned_today': points_earned_today,
                 'unclaimed_tasks_count': unclaimed_tasks_count,
                 'unclaimed_points': unclaimed_points,
                 'unstarted_count': unstarted_count,
                 'in_progress_count': in_progress_count,
                 'bulletins': bulletins,}
        return render(request, 'users/dashboard.html', values) 


##in current iteration creates a new chore
    ## then credits that chore as complete to the desired user
def bonus_points(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BonusPointsForm(request.POST)
            uProfile = Profile.objects.get(user = request.user)
            if form.is_valid():
                uName = request.user.username
                bonusMember = form.cleaned_data['member_name']
                points = form.cleaned_data['bonus_points']

                
                bonusMember = User.objects.get(username = bonusMember)
                bonusProfile = Profile.objects.get(user = bonusMember)


                taskName = 'Kudos for {member}'.format(member = bonusMember)
                taskBody = '{uName} thinks {member} deserves a {points} point bonus!'.format(uName = uName, member = bonusMember, points = points)

                kudos = Task.objects.create(title=taskName, body=taskBody, points=points, claimed=True,
                task_status=True, user_created=uProfile, user_claimed=bonusProfile, household=(uProfile.household))
                bonusProfile.modify_points(points, kudos)

                
                return redirect('/')

    form = BonusPointsForm()
    return render(request, 'users/giveBonus.html', {'form': form})

##in current iteration creates a new chore
    ## then credits that chore as complete to the desired user
def minus_points(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MinusPointsForm(request.POST)
            uProfile = Profile.objects.get(user = request.user)
            if form.is_valid():
                uName = request.user.username
                minusMember = form.cleaned_data['member_name']
                points = form.cleaned_data['minus_points']
                points = -points

                
                minusMember = User.objects.get(username = minusMember)
                minusProfile = Profile.objects.get(user = minusMember)


                taskName = 'Bad for {member}'.format(member = minusMember)
                taskBody = '{uName} thinks {member} deserves a {points} point reduction!'.format(uName = uName, member = minusMember, points = points)

                minus = Task.objects.create(title=taskName, body=taskBody, points=points, claimed=True,
                task_status=True, user_created=uProfile, user_claimed=minusProfile, household=(uProfile.household))
                minusProfile.modify_points(points, minus)

                
                return redirect('/')

    form = MinusPointsForm()
    return render(request, 'users/joinHousehold.html', {'form': form})


def bidding(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BiddingForm(request.POST)
            uProfile = Profile.objects.get(user=request.user)
            if form.is_valid():
                uName = request.user.username
                bid = form.clean_bid()
                task_bid = form.cleaned_data['unclaimed_tasks']

                task_bid = Task.objects.get(pk=task_bid.id)
                task_bid.points = bid
                task_bid.user_claimed = uProfile
                task_bid.save()

                return redirect('/')


    form = BiddingForm()
    return render(request, 'users/bidding.html', {'form': form})


def tasks(request):
    if request.user.is_authenticated:
        task_assign(request)
        lfn = last_fortnight()
        
        household = request.user.profile.household
        user = request.user
        tasks = household.task_set.all()
        unclaimed_tasks = list(tasks.filter(claimed=False))
        todo_tasks = list(tasks.filter(claimed=True).filter(in_progress=False).filter(task_status=False))
        in_prog_tasks = list(tasks.filter(in_progress=True))
        complete_tasks = tasks.filter(task_status=True)
        complete_tasks = list(complete_tasks.filter(due_date__gte=lfn))
        movable_tasks = todo_tasks + in_prog_tasks + complete_tasks
        values = {'user': user,
                  'unclaimed_tasks': unclaimed_tasks,
                  'todo_tasks': todo_tasks,
                  'in_prog_tasks': in_prog_tasks,
                  'complete_tasks': complete_tasks,
                  'movable_tasks': movable_tasks}

        if request.method == "POST":
            try: 
                payload = json.loads(request.body)
                handle_task_ajax(request, payload)
            except:
                create_task(request)
                return redirect('taskboard')

        return render(request, 'users/task-board.html', values)


def task_assign(request):
    bid_end = timezone.now() + timezone.timedelta(days=-1)  # bids end after this amount of days
    unclaimed_tasks = Task.objects.filter(claimed='False', creation_time__gte=bid_end)
    for task in unclaimed_tasks:
        if task.user_claimed is not None:
            task.claimed = True
        else:
            profiles = request.user.profile.household.members.all()
            selected_profile = random.choice(list(profiles))
            task.user_claimed = selected_profile
        task.save()


def last_fortnight():   
    #Calculates first and third monday of current month chooses most recent of two slowly
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    monthcal = c.monthdatescalendar(year, month)
    first_third_mon = [day for week in monthcal for day in week if \
                       day.weekday() == calendar.MONDAY and \
                       day.month == month]
    del first_third_mon[1] #Deletes second Monday
    del first_third_mon[2] #Deletes fourth Monday
    last_fortnight = first_third_mon[1] if datetime.date.today() > first_third_mon[1] else first_third_mon[0]
    return last_fortnight


def handle_task_ajax(request, payload):
    if payload.get("type") == "user_bid":
        task_id = payload.get("id")
        task = Task.objects.get(pk=task_id)
        task.points = payload.get("bid")
        task.user_claimed = request.user.profile
        task.save()
    if payload.get("type") == "task_move":
        task_id = payload.get("id")
        task = Task.objects.get(pk=task_id)
        task_status = payload.get("new_pos")
        if task_status == "to-do-column":
            task.in_progress = False
            task.task_status = False
        elif task_status == "in-prog-column":
            task.in_progress = True
            task.task_status = False
        elif task_status == "complete-column":
            task.in_progress = False
            task.task_status = True
        else:
            pass
        task.save()


def create_task(request):
    household = request.user.profile.household
    form = request.POST
    form_data = form.dict()
    # Task information
    profile_created = request.user.profile
    task_title = form_data['task_title']
    task_body = form_data['task_body']
    due_datetime = form_data['due_date'] + " " + "12:00:00"  # currently we have no way to use a given dateform_data['due_time']
    due_datetime = timezone.make_aware(datetime.datetime.strptime(due_datetime, '%Y-%m-%d %H:%M:%S'))
    task = Task.objects.create(title = task_title,
                                body = task_body,
                                creation_time = timezone.now(),
                                due_date = due_datetime,
                                points = 1000,
                                user_created = profile_created,
                                household = household)
    # Frequency information
    try:
        if 'repeats' in form_data:
            frequency = form_data['repeat-type-radio']
            if frequency == 'weekly':
                mo = tu = we = th = fr = sa = su = False
                if 'mo' in form_data:
                    mo = True
                if 'tu' in form_data:
                    tu = True
                if 'we' in form_data:
                    we = True
                if 'th' in form_data:
                    th = True
                if 'fr' in form_data:
                    fr = True
                if 'sa' in form_data:
                    sa = True
                if 'su' in form_data:
                    su = True
                recurrence = TaskRecurrence.objects.create(task_to_clone = task,
                                                           frequency = frequency,
                                                           mo = mo,
                                                           tu = tu,
                                                           we = we,
                                                           th = th,
                                                           fr = fr,
                                                           sa = sa,
                                                           su = su,)
            else:
                day_of_month = form_data['day_of_month']
                recurrence = TaskRecurrence.objects.create(task_to_clone = task,
                                                           frequency = frequency,
                                                           day_of_month = day_of_month)
    except:
        print("Something went wrong")

    form = BiddingForm()
    return render(request, 'users/bidding.html', {'form': form})

def open_Lootbox(request):
    if request.user.is_authenticated:

        if request.method == 'POST':


            uName = request.user.username
            uMember = User.objects.get(username=uName)
            uProfile = Profile.objects.get(user=uMember)


            if uProfile.lootboxes > 0:

                uProfile.open_lootbox()
                newBox = Lootbox.objects.create(owner=uProfile)
                newBox.generateNounAdjectivePair()

                messages.info(
                    request, 'You have opened the lootbox!'
                )

                '''
                uName = request.user.username
                minusMember = form.cleaned_data['member_name']
                points = form.cleaned_data['minus_points']
                points = -points

                
                minusMember = User.objects.get(username = minusMember)
                minusProfile = Profile.objects.get(user = minusMember)


                taskName = 'Bad for {member}'.format(member = minusMember)
                taskBody = '{uName} thinks {member} deserves a {points} point reduction!'.format(uName = uName, member = minusMember, points = points)

                minus = Task.objects.create(title=taskName, body=taskBody, points=points, claimed=True,
                task_status=True, user_created=uProfile, user_claimed=minusProfile, household=(uProfile.household))
                minusProfile.modify_points(points, minus)
                '''
            return redirect('/')

        return render(request, 'users/openLootbox.html')


def log(request):
    if request.user.is_authenticated:
        task_assign(request)
        uHousehold = Profile.objects.get(user=request.user).household
        tasks_finished = Task.objects.filter(household=uHousehold, claimed='True', task_status='True')
        tasks_in_progress = Task.objects.filter(household=uHousehold, claimed='True', task_status='False')
        tasks_unclaimed = Task.objects.filter(claimed='False')
        values = {'tasks_finished': tasks_finished,
                  'tasks_in_progress': tasks_in_progress,
                  'tasks_unclaimed': tasks_unclaimed, }
        return render(request, 'users/log.html', values)

def profilePicture(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = profilePictureForm(request.POST,request.FILES)
            if form.is_valid():
                uProfile = Profile.objects.get(user=request.user)
                image_path = uProfile.profile_picture.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                profilePicture = form.cleaned_data['profilePicture']
                uProfile.profile_picture = profilePicture
                uProfile.save()
                return redirect('/')


'''        household = request.user.profile.household
        householdMembers = household.members.all()
        mList = []
        for queries in householdMembers:
            mList.append(queries.user.username)
            print(queries.user.username)
        print(mList)

        try:
            selected_choice = household.member_set.get(pk=request.POST['choice'])
        except (KeyError, User.DoesNotExist):
            return render(request, 'users/listMembers.html', {
                'household': household,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.modify_points(self, )

        return render(request, 'users/listMembers.html',{household.name:mList})
        return JsonResponse({household.name:mList}, safe = False)

        return HttpResponse("HOWDY!!")
'''        
