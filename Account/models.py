from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible


class IndexTable(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    own_room_num = models.IntegerField(default=5)
    interviewee_list = models.ManyToManyField("Account.Interviewee")

    def __str__(self):
        if self.user_id != 0:
            user = User.objects.get(id=self.user_id)
            return user.username + " owning " + str(self.own_room_num) + " rooms "
        else:
            return str(self.user_id) + " owning " + str(self.own_room_num) + " rooms"


@deconstructible
class Interviewer(models.Model):
    username = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username


@deconstructible
class Interviewee(models.Model):
    username = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    telephone = models.CharField(max_length=20, default="")
    addr = models.CharField(max_length=200, default="")
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.username
