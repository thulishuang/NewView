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
            return Response(data="authenticated", status=status.HTTP_200_OK)
        return Response(data="unauthenticated", status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == "POST":
        serializer = ManagerSerializer(request.data)
        if serializer.is_valid():
            return Response(data="authenticated", status=status.HTTP_200_OK)
        else:
            return Response(data="unauthenticated", status=status.HTTP_401_UNAUTHORIZED)


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
