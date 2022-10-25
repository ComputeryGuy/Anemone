from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

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
