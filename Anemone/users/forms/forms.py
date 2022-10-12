from django import forms


class BulletinForm(forms.Form):
    bulletin_body = forms.CharField(max_length=500)
    expire_time = forms.DateTimeField()

class HouseholdCreateForm(forms.Form):
    household_name = forms.CharField(max_length=32)
    household_pin = forms.CharField(max_length=32)

class JoinGroupForm(forms.Form):
    household_pin = forms.IntegerField()