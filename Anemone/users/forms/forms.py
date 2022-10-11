from django import forms


class BulletinForm(forms.Form):
    bulletin_body = forms.CharField(max_length=500)
    expire_time = forms.DateTimeField()
