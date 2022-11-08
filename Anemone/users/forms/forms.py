from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.core.exceptions import ValidationError

from django.db import models
from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext_lazy as _
from users.models import Household, Profile, Task


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

class BiddingForm(forms.Form):
    unclaimed_tasks = forms.ModelChoiceField(queryset=Task.objects.filter(task_status='False'))
    bid = forms.IntegerField()

    def clean_bid(self):
        bid = self.cleaned_data["bid"]
        task_bid = self.cleaned_data["unclaimed_tasks"]
        if task_bid.user_claimed is not None and bid >= task_bid.points or task_bid.user_claimed is None and bid > task_bid.points:
            raise ValidationError(_('Bid is too great. Bid lower.'), code='invalidBid')
        return bid


class BiddingForm(forms.Form):
    unclaimed_tasks = forms.ModelChoiceField(queryset=Task.objects.filter(task_status='False'))
    bid = forms.IntegerField()

    def clean_bid(self):
        bid = self.cleaned_data["bid"]
        task_bid = self.cleaned_data["unclaimed_tasks"]
        if task_bid.user_claimed is not None and bid >= task_bid.points or task_bid.user_claimed is None and bid > task_bid.points:
            raise ValidationError(_('Bid is too great. Bid lower.'), code='invalidBid')
        return bid

    '''    member_selected = forms.CharField(label = 'Which user deserves extra points this week?',
        widget = forms.RadioSelect(choices = ))

        def __init__(self, [''], *args, **kwargs):
            super(BonusPointsForm, self).__init__(*args, **kwargs)

            for 
    '''
