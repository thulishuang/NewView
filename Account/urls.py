from django.conf.urls import url
from .views import AccountLogin, AccountLogout, AccountDetail, AccountService, AccountRoomList


urlpatterns = [
    # user login
    url(r'^login$', AccountLogin.as_view()),
    # user logout
    url(r'^logout$', AccountLogout.as_view()),
    # user detail
    url(r'^detail$', AccountDetail.as_view()),
    # service alteration
    url(r'^service$', AccountService.as_view()),
    # room list
    url(r'^roomlist$', AccountRoomList.as_view()),

]