from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Sum, Count
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,  # On delete of user, profile is deleted
        primary_key=True,
    )
    #tasks_finished = Chore.objects.filter(user_claimed=user).annotate(tasks_finished=Count('task_status').filter(task_status='True'))
    #points = Chore.objects.filter(user_claimed=user, task_status='True').annotate(points=Sum('points'))
    points = models.IntegerField(default=0, verbose_name="points")
    tasks_finished = models.IntegerField(default=0, verbose_name="tasks finished")

    def modify_points(self, points): #add in views when task is marked as complete
        self.points = points
        chore = Chore.objects.filter(user_claimed=self.user, task_status='True').annotate(tasks_count=Count('task_status'))
        self.tasks_finished = chore[0].tasks_count
        self.save()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    points: int = Chore.objects.filter(user_claimed=instance, task_status='True').annotate(points_added=Sum('points'))
    if instance.profile.points != points:
        instance.profile.modify_points(points[0].points_added)
    instance.profile.save()


class Bulletin(models.Model):
    user = models.CharField(max_length=500)
    bulletin_body = models.CharField(max_length=500)
    creation_time = models.DateTimeField()
    expire_time = models.DateTimeField()


class Event(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    datetime = models.DateTimeField()


class Chore(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    due_date = models.DateTimeField()
    points = models.IntegerField()
    user_created = models.CharField(max_length=500)
    user_claimed = models.CharField(max_length=500, default=None)
    task_status = models.BooleanField(default=False)


class Household(models.Model):
    name = models.CharField(max_length = 30, default = "NO NAME!")
    profiles = models.ManyToManyField(Profile, blank = True)
    messages = models.ManyToManyField(Bulletin, blank = True)
    events = models.ManyToManyField(Event, blank = True)
    chores = models.ManyToManyField(Chore, blank = True)

    pin = models.IntegerField(unique = True)

#class Pin(models.Model):
#    pin = models.IntegerField(unique=True)
#    attached_group = models.ForeignKey(Household)
    
