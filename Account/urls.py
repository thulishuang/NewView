from django.conf.urls import url
from .views import AccountLogin, AccountLogout, AccountDetail


urlpatterns = [
    url(r'^login$', AccountLogin.as_view()),
    url(r'^logout$', AccountLogout.as_view()),
    url(r'^detail$', AccountDetail.as_view()),
    # todo: edit room information (change attributes; open or close; add interviewer; add interviewee)
    # todo: add interviewee
    # todo: edit interviewee information (change attributes; delete)
    # todo: alter service (pay fee; expand room numbers)
]
