from django.views import View
from django.core.exceptions import *
from .models import Manager

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


class Login(View):
    def get(self, request):
        if 'status' in request.session:
            if request.session['status']:
                return
        raise ValidationError("no user log in")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Manager.objects.get(username=username, password=password)
            request.session['status'] = True
            request.session['username'] = username
            return
        except Manager.DoesNotExist:
            raise ValidationError("wrong username or password")


class Logout(View):
    def post(self, request, *args, **kwargs):
        try:
            request.session['status'] = False
            request.session['username'] = ''
        except:
            raise ValidationError("failed to log user out")


class RoomList(View):
    def get(self, request):
        return


class CloseRoom(View):
    def get(self, request):
        return

    def post(self, request):
        return


class IntervieweeList(View):
    def get(self, request):
        return

    def post(self, request):
        return


class DeleteInterviewee(View):
    def get(self, request):
        return

    def  post(self, request):
        return


class AddInterviewee(View):
    def get(self, request):
        return

    def post(self, request):
        return
