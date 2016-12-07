from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible


@deconstructible
class Manager(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    own_room_num = models.IntegerField(default=0)
    outdate_time = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

    def __int__(self):
        if self.id:
            return self.id
        else:
            return 1


@deconstructible
class Interviewer(models.Model):
    username = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username

    def __int__(self):
        if self.id:
            return self.id
        else:
            return 1


@deconstructible
class Interviewee(models.Model):
    username = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    telephone = models.CharField(max_length=20, default="")
    addr = models.CharField(max_length=200, default="")
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def __int__(self):
        if self.id:
            return self.id
        else:
            return 1
