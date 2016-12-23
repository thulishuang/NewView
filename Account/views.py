from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manager
from .serializer import ManagerSerializer

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        if request.user:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        try:
            user = Manager.objects.get(username=username, password=password)
            request.user = user
            return Response(status=status.HTTP_202_ACCEPTED)
        except Manager.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


def logout(request):
    try:
        request.user = None
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_410_GONE)


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
