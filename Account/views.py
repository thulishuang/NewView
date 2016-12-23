from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manager
from Room.models import Room
from .serializer import ManagerSerializer, AuthenticationSerializer

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
            return Response(data=0,status=status.HTTP_202_ACCEPTED)
        except Manager.DoesNotExist:
            return Response(data=1,status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def logout(request):
    try:
        request.user = None
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_410_GONE)


@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == "GET":
        user = request.user
        user_data = {
            'username': user.username,
            'own_room_num': user.own_room_num,
        }

        return Response(status=status.HTTP_200_OK)


def close_room(request):
    return


def interviewee_list(request):
    return


def delete_interviewee(request):
    return


def add_interviewee(request):
    return
