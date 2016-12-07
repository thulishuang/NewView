from django.db import models
from django.utils import timezone


class Manager(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    own_room_num = models.IntegerField()
    own_room_list = models.ManyToManyField('Room.Room')
    outdate_time = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username


class Interviewer(models.Model):
    username = models.CharField(max_length=50)


class Interviewee(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    addr = models.CharField(max_length=200)
    state = models.BooleanField(default=False)