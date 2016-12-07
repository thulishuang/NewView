from django.db import models
from Account.models import Manager, Interviewee, Interviewer


# Create your models here.
class Room(models.Model):
    index = models.IntegerField(default=1)
    url = models.URLField()  # /room/username/room_title
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    state = models.BooleanField(default=False)  # true: open, false: close
    manager = models.ForeignKey(Manager)
    interviewer = models.OneToOneField(Interviewer)
    interviewees = models.ManyToManyField(Interviewee)

    def __str__(self):
        return self.title
