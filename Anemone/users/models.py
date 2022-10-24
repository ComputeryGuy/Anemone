import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


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

    def modify_points(self, points, chore):  # add in views when task is marked as complete
        self.points += points
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


class Event(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    datetime = models.DateTimeField()


class Chore(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    due_date = models.DateTimeField()
    points = models.IntegerField()
    claimed = models.BooleanField(default=False)
    task_status = models.BooleanField(default=False)  # finished/not
    user_created = models.ForeignKey(Profile, default=None, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='chore_user_created')
    user_claimed = models.ForeignKey(Profile, default=None, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='chore_user_claimed')


@receiver(pre_save, sender=Chore)
def cache_previous_status(sender, instance, *args, **kwargs):
    if not instance._state.adding:
        original_status = None
        if instance.user_claimed is not None:
            original_status = Chore.objects.get(pk=instance.id).task_status

        instance.__original_status = original_status
    else:
        instance.__original_status = None


@receiver(post_save, sender=Chore)
def point_updater(sender, instance, **kwargs):
    if instance.task_status != instance.__original_status and instance.user_claimed is not None and instance.__original_status is not None:
        profile = instance.user_claimed
        if instance.task_status:
            profile.modify_points(instance.points, instance)
        else:
            profile.modify_points(-instance.points, instance)


class Household(models.Model):
    household_id = models.UUIDField(primary_key=True,
                                    default = uuid.uuid4,
                                    editable = False)
    name = models.CharField(max_length = 30, default = "NO NAME!")
    profiles = models.ManyToManyField(Profile, blank = True)
    bulletins = models.ManyToManyField(Bulletin, blank = True)
    events = models.ManyToManyField(Event, blank = True)
    chores = models.ManyToManyField(Chore, blank = True)

    pin = models.IntegerField(unique = True)

#class Pin(models.Model):
#    pin = models.IntegerField(unique=True)
#    attached_group = models.ForeignKey(Household)
