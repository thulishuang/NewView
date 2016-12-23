from rest_framework import authentication
from rest_framework import exceptions
from .models import Manager


class ManagerAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('username')
        password = request.META.get('password')
        if not username:
            return None

        try:
            user = Manager.objects.get(username=username, password=password)
        except Manager.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None
