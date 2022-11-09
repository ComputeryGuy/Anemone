"""Anemone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('bulletin/', user_views.post_bulletin, name='bulletin'),
    path('createTask/', user_views.create_task, name='createTask'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('createHousehold/', user_views.create_household, name='createGroup'),
    path('joinHousehold/', user_views.join_household, name='joinGroup'),

    ##used if url join is implemented
    #path('joinHousehold/<uuid:household_id>/', user_views.join_household, name='joinGroup'),
    
    ##currently generates a link that will point to the above unimplimented url
    path('generate_household_link/', user_views.generate_household_link, name="generateLink"),


    path('<uuid:household_id>', user_views.dashboard, name="dashboard"),
    path('bonus_points/', user_views.bonus_points, name="bonusPoints"),
    path('minus_points/', user_views.minus_points, name="minusPoints"),
    path('bidding/',  user_views.bidding, name='bidding'),
    path('<uuid:household_id>/tasks', user_views.tasks, name="taskboard"),
]
