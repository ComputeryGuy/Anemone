import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Household(models.Model):
    household_id = models.UUIDField(primary_key=True,
                                    default = uuid.uuid4,
                                    editable = False)
    name = models.CharField(max_length = 30, default = "NO NAME!")

    pin = models.IntegerField(unique = True)


class Profile(models.Model):
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,      # On delete of user, profile is deleted
            primary_key=True,
    )
    # tasks_finished = Chore.objects.filter(user_claimed=user).annotate(tasks_finished=Count('task_status').filter(task_status='True'))
    # points = Chore.objects.filter(user_claimed=user, task_status='True').annotate(points=Sum('points'))

    points = models.IntegerField(default=0, verbose_name="points")
    tasks_finished = models.IntegerField(default=0, verbose_name="tasks finished")
    household = models.ForeignKey(Household, default=None, on_delete=models.CASCADE, null=True, related_name = "members")


    ## game aspects
    xp = models.IntegerField(default=0, verbose_name="xp")
    level = models.IntegerField(default=0)
    nextLevelThresh = models.IntegerField(default=1000)
    prevLevelThresh = models.IntegerField(default=0)
    xpToNextLevel = models.IntegerField(default=1000)

    def update_levelSystem(self, points):
            self.xp += points
            

            while self.xp > self.nextLevelThresh:
                self.level += 1
                self.update_levelThresh(self.level, self.nextLevelThresh)
            
            self.update_xpToNextLevel(self.xp, self.nextLevelThresh)


    def update_levelThresh(self, level, nextLevelThresh):
        self.prevLevelThresh = nextLevelThresh
        self.nextLevelThresh = 1000 * ((level)**2 + 2)
    
    def update_xpToNextLevel(self, xp, nextLevelThresh):
        self.xpToNextLevel = nextLevelThresh - xp




    def modify_points(self, points, chore):  # add in views when task is marked as complete
        self.points += points
        
        self
        ##update xp / level if necessary
        if points > 0:
            self.update_levelSystem( points)

        if chore.task_status:
            self.tasks_finished += 1
        else:
            self.tasks_finished -= 1
        self.save()
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Bulletin(models.Model):
    user = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    bulletin_body = models.CharField(max_length=500)
    creation_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    household = models.ForeignKey(Household, default=None, on_delete=models.CASCADE, null=True)


class Event(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    datetime = models.DateTimeField()


class Task(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    points = models.IntegerField()
    claimed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    task_status = models.BooleanField(default=False)  # finished/not
    user_created = models.ForeignKey(Profile, default=None, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='task_user_created')
    user_claimed = models.ForeignKey(Profile, default=None, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='task_user_claimed')
    household = models.ForeignKey(Household, default=None, on_delete=models.CASCADE, null=True)


class TaskRecurrence(models.Model):
    #Recurrence Info
    task_to_clone = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=8)
    mo = models.BooleanField(default=False)
    tu = models.BooleanField(default=False)
    we = models.BooleanField(default=False)
    th = models.BooleanField(default=False)
    fr = models.BooleanField(default=False)
    sa = models.BooleanField(default=False)
    su = models.BooleanField(default=False)
    day_of_month = models.IntegerField(null=True, blank=True)


@receiver(pre_save, sender=Task)
def cache_previous_status(sender, instance, *args, **kwargs):
    if not instance._state.adding:
        original_status = None
        if instance.user_claimed is not None:
            original_status = Task.objects.get(pk=instance.id).task_status

        instance.__original_status = original_status
    else:
        instance.__original_status = None


@receiver(post_save, sender=Task)
def point_updater(sender, instance, **kwargs):
    if datetime.now() >= timezone.make_naive((instance.creation_time + timedelta(days=1))) and not instance.claimed and instance.user_claimed is not None:
        instance.claimed = 'True'
        instance.save()
    if instance.task_status != instance.__original_status and instance.user_claimed is not None and instance.__original_status is not None:
        profile = instance.user_claimed
        if instance.task_status:
            profile.modify_points(instance.points, instance)
        else:
            profile.modify_points(-instance.points, instance)



#class Pin(models.Model):
#    pin = models.IntegerField(unique=True)
#    attached_group = models.ForeignKey(Household)
