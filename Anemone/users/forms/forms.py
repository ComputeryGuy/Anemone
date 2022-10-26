from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from django.db import models
from django.forms import ModelForm

from users.models import Household, Profile

class BulletinForm(forms.Form):
    bulletin_body = forms.CharField(max_length=500)
    expire_time = forms.DateTimeField()


class HouseholdCreateForm(forms.Form):
    household_name = forms.CharField(max_length=32)
    household_pin = forms.CharField(max_length=32)


class JoinGroupForm(forms.Form):
    household_pin = forms.IntegerField()


class DateTimeForm(forms.Form):
    due_date = forms.DateField(widget=AdminDateWidget())
    due_time = forms.DateField(widget=AdminTimeWidget())



class BonusPointsForm(forms.Form):
    member_name = forms.CharField(max_length=32)
    bonus_points = forms.IntegerField()

class MinusPointsForm(forms.Form):
    member_name = forms.CharField(max_length=32)
    minus_points = forms.IntegerField()




    '''    member_selected = forms.CharField(label = 'Which user deserves extra points this week?',
        widget = forms.RadioSelect(choices = ))

        def __init__(self, [''], *args, **kwargs):
            super(BonusPointsForm, self).__init__(*args, **kwargs)

            for 
    '''