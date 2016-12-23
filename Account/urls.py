from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^detail/room_list$', room_list, name="roomlist"),
    url(r'^detail/room_list/close$', close_room, name="closeroom"),
    url(r'^detail/interviewee_list$', interviewee_list, name="intervieweelist"),
    url(r'detail/interviewee_list/delete$', delete_interviewee, name="delete_interviewee"),
    url(r'detail/interviewee_list/add$', add_interviewee, name="add_interviewee"),
]
