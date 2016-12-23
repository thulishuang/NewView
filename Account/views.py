from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manager
from Room.models import Room

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        if request.user:
            return Response(data={
               'error_code': 0
            }, status=status.HTTP_200_OK)
        return Response(data={
            'error_code': 0
        }, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        try:
            user = Manager.objects.get(username=username, password=password)
            request.user = user
            return Response(data={
                'error_code': 0
            }, status=status.HTTP_202_ACCEPTED)
        except Manager.DoesNotExist:
            return Response(data={
               'error_code': 1
            }, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def logout(request):
    try:
        request.user = None
        return Response(data={
            'error_code': 0
        }, status=status.HTTP_200_OK)
    except:
        return Response(data={
            'error_code': 1
        }, status=status.HTTP_410_GONE)


@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == "GET":
        user = request.user
        user_data = {
            'username': user.username,
            'room_num': user.own_room_num,
        }
        room_list = Room.objects.filter(manager=user)
        room_data = [
            {
                'num': r.id,
                'title': r.title,
                'description': r.description,
                'state': r.state,
                'interviewer_name': r.interviewer.username
            } for r in room_list
        ]
        return Response(data={
            'user': user_data,
            'roomlist': room_data
        }, status=status.HTTP_200_OK)

    elif request.method == "POST":
        post_data = {
            'roomnum': int(request.data['roomnum']),
            'title': request.data['title'],
            'description': request.data['description']
        }
        room = Room.objects.get(pk=post_data['roomnum'])
        try:
            room.title = post_data['title']
            room.description = post_data['description']
            room.save()
            return Response(data={
                'error_code': 0
            }, status=status.HTTP_200_OK)
        except:
            return Response(data={
                'error_code': 1
            }, status=status.HTTP_200_OK)


def close_room(request):
    return


def interviewee_list(request):
    return


def delete_interviewee(request):
    return


def add_interviewee(request):
    return
