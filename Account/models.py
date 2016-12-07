from django.db import models
from django.utils import timezone


class Manager(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    own_room_num = models.IntegerField()
    outdate_time = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username
