from django.db import models
from Account.models import Manager, Interviewee, Interviewer


class Room(models.Model):
    url = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    state = models.BooleanField(default=False)
    manager = models.ForeignKey(Manager)
    interviewer = models.OneToOneField(Interviewer, default=Interviewer())
    interviewees = models.ManyToManyField(Interviewee)

    def __str__(self):
        return self.title
