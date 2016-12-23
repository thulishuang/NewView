from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.core.exceptions import *
from .models import Manager
from .serializer import ManagerSerializer

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        if 'status' in request.session:
            if request.session['status']:
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTPP_401_UNAUTHORIZED)

    elif request.method == "POST":
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            request.session['status'] = True
            request.session['username'] = request.POST['username']
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


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


def add_interviewe(request):
    return
