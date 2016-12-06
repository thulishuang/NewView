from django.db import models
from Account.models import Manager


# Create your models here.
class Room(models.Model):
    url = models.URLField()  # /room/username/room_title
    title = models.CharField(max_length=200)
    state = models.BooleanField()  # true: open, false: close
    manager = models.ManyToManyField(Manager)

