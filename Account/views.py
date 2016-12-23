from django.http import HttpResponse
from django.core.exceptions import *
from .models import Manager
from .serializer import ManagerSerializer

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


def login(request):
    if request.method == "GET":
        if 'status' in request.session:
            if request.session['status']:
                return HttpResponse("logged", type="text/plain", status=200)
        return HttpResponse("none", type="text/plain", status=401)

    elif request.method == "POST":
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            request.session['status'] = True
            request.session['username'] = request.POST['username']
            return HttpResponse("logged", type="text/plain", status=200)
        else:
            return HttpResponse("none", type="text/plain", status=401)


def logout(request):
    return


def room_list(request):
    return


def close_room(request):
    return


def interviewee_list(request):
    return


def delete_interviewee(request):
    return


def add_interviewee(request):
    return
