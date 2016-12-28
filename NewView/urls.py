from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/account/', include('Account.urls')),
    # url(r'^room/', include('Room.urls')),
]
