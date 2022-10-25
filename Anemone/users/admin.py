from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Household)
admin.site.register(Bulletin)
admin.site.register(Event)
admin.site.register(Chore)
admin.site.register(TaskRecurrence)
