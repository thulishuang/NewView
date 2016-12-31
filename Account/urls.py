from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^login$', user_login, name="login"),
    url(r'^logout$', user_logout, name="logout"),
    url(r'^detail/room_list$', room_list, name="roomlist"),
    url(r'^detail/room_list/invite_interviewer$', invite_interviewer, name="invite_interviewer"),
    url(r'^detail/room_list/change$', change_room, name="changeroom"),
    url(r'^detail/interviewee_list$', interviewee_list, name="intervieweelist"),
    url(r'detail/interviewee_list/delete$', delete_interviewee, name="delete_interviewee"),
    url(r'detail/interviewee_list/send_mail$', send_mail, name="send_mail"),
]
