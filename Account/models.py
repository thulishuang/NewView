from django.db import models
from django.utils import timezone


class Manager(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    own_room_num = models.IntegerField()
    outdate_time = models.TimeField(default=timezone.datetime.now())
