from django.contrib import admin
from .models import IndexTable, Interviewer, Interviewee

# Register your models here.
admin.site.register(IndexTable)
admin.site.register(Interviewee)
admin.site.register(Interviewer)