from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^login$', Login.as_view(), name="login"),
    url(r'^logout$', Logout.as_view(), name="logout"),
    url(r'^detail/room_list$', RoomList.as_view(), name="roomlist"),
    url(r'^detail/room_list/close$', CloseRoom.as_view(), name="closeroom"),
    url(r'^detail/interviewee_list$', IntervieweeList.as_view(), name="intervieweelist"),
]
