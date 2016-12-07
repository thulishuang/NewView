from django.contrib import admin
from .models import Manager, Interviewer, Interviewee

# Register your models here.
admin.site.register(Manager)
admin.site.register(Interviewee)
admin.site.register(Interviewer)