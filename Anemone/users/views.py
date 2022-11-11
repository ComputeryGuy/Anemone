import datetime
import calendar
import json
from pathlib import Path

from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from .forms.forms import *
from .models import *

from django.http import HttpResponse
from django.http import JsonResponse

from django.forms.models import model_to_dict

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.household is not None:
            uuid = str(request.user.profile.household.household_id)
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
                print("wah")
                user = request.user.username
                bulletin_body = form.cleaned_data['bulletin_body']
                creation_time = datetime.datetime.now(datetime.timezone.utc)
                expire_time = form.cleaned_data['expire_time']
                bulletin = Bulletin.objects.create(user=user,
                                                   bulletin_body=bulletin_body,
                                                   creation_time=creation_time,
                                                   expire_time=expire_time, 
                                                   household = request.user.profile.household_set.all()[0])
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
        
    


def dashboard(request, household_id):
    if request.user.is_authenticated:
        bidEnd = datetime.datetime.now() + datetime.timedelta(days=-1)  # bids end after this amount of days
        unclaimed_tasks = Task.objects.filter(claimed='False', creation_time__lte=bidEnd)
        for object in unclaimed_tasks:
            object.save()
        household = get_object_or_404(Household, pk=household_id)
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


def tasks(request, household_id):
    bidEnd = datetime.datetime.now() + datetime.timedelta(days=-1)  # bids end after this amount of days
    unclaimed_tasks = Task.objects.filter(claimed='False', creation_time__lte=bidEnd)
    for object in unclaimed_tasks:
        object.save()
    lfn = last_fortnight()
    
    household = get_object_or_404(Household, pk=household_id)
    user = request.user
    tasks = household.task_set.all()
    unclaimed_tasks = list(tasks.filter(claimed=False))
    todo_tasks = list(tasks.filter(claimed=True).filter(in_progress=False).filter(task_status=False))
    in_prog_tasks = list(tasks.filter(in_progress=True))
    complete_tasks = tasks.filter(task_status=True)
    complete_tasks = list(complete_tasks.filter(due_date__gte=lfn))
    movable_tasks = todo_tasks + in_prog_tasks + complete_tasks
    values = {'household_id': household_id,
              'user': user,
              'unclaimed_tasks': unclaimed_tasks,
              'todo_tasks': todo_tasks,
              'in_prog_tasks': in_prog_tasks,
              'complete_tasks': complete_tasks,
              'movable_tasks': movable_tasks}

    if request.user.is_authenticated:
        if request.method == "POST":
            try: 
                payload = json.loads(request.body)
                handle_task_ajax(payload)
            except:
                create_task(request, household_id)
                return redirect('taskboard', household_id=household_id)

        return render(request, 'users/task-board.html', values)


def last_fortnight():   
    #Calculates first and third monday of current month chooses most recent of two slowly
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    year = datetime.date.today().year
    month = datetime.date.today().month
    monthcal = c.monthdatescalendar(year, month)
    first_third_mon = [day for week in monthcal for day in week if \
                       day.weekday() == calendar.MONDAY and \
                       day.month == month]
    del first_third_mon[1] #Deletes second Monday
    del first_third_mon[2] #Deletes fourth Monday
    last_fortnight = first_third_mon[1] if datetime.date.today() > first_third_mon[1] else first_third_mon[0]
    return last_fortnight


def handle_task_ajax(payload):
    if payload.get("type") == "user_bid":
        task_id = payload.get("id")
        task = Task.objects.get(pk=task_id)
        task.points = payload.get("bid")
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


def create_task(request, household_id):
    form = request.POST
    form_data = form.dict()
    # Task information
    profile_created = request.user.profile
    task_title = form_data['task_title']
    task_body = form_data['task_body']
    due_datetime = form_data['due_date'] + " " + "12:00:00"  # currently we have no way to use a given dateform_data['due_time']
    due_datetime = datetime.datetime.strptime(due_datetime, '%Y-%m-%d %H:%M:%S')
    task = Task.objects.create(title = task_title,
                                body = task_body,
                                creation_time = datetime.now,
                                due_date = due_datetime,
                                points = 1000,
                                user_created = profile_created,
                                household = Household.objects.get(pk=household_id))
    # Frequency information
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

def log(request):
    if request.user.is_authenticated:
        bidEnd = datetime.datetime.now() + datetime.timedelta(days=-1)  # bids end after this amount of days
        unclaimed_tasks = Task.objects.filter(claimed='False', creation_time__lte=bidEnd)
        for object in unclaimed_tasks:
            object.save()
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
                print('profilePicture starts')
                uProfile = Profile.objects.get(user=request.user)
                '''if ImageFieldFile is not None:
                    print('1')
                    if Path.exists(uProfile.profile_picture.url):
                        Path.unlink(uProfile.profile_picture.url)'''
                profilePicture = form.cleaned_data['profilePicture']
                uProfile.profile_picture = profilePicture
                uProfile.save()
                print('profilePicture ends')
                return redirect('/')



    form = profilePictureForm()
    return render(request, 'users/profilePicture.html', {'form': form})

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
