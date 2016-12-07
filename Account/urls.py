from django.conf.urls import url
from .views import AccountLogin, AccountLogout, AccountDetail, EditRoom


urlpatterns = [
    url(r'^login$', AccountLogin.as_view()),
    url(r'^logout$', AccountLogout.as_view()),
    url(r'^detail$', AccountDetail.as_view()),
    # todo: edit room information (change attributes; open or close; add interviewer; add interviewee)
    url(r'^editroom/', EditRoom.as_view()),
    # todo: add interviewee
    # todo: edit interviewee information (change attributes; delete)
    # todo: alter service (pay fee; expand room numbers), --currently abandoned
]
