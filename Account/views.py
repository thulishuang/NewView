from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manager, Interviewee
from Room.models import Room

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        if request.user:
            return Response(data={
               'error_code': 0
            }, status=200)
        return Response(data={
            'error_code': 0
        }, status=204)

    elif request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        try:
            user = Manager.objects.get(username=username, password=password)
            request.user = user
            return Response(data={
                'error_code': 0
            }, status=202)
        except Manager.DoesNotExist:
            return Response(data={
               'error_code': 1
            }, status=202)


@api_view(['POST'])
def logout(request):
    try:
        request.user = None
        return Response(data={
            'error_code': 0
        }, status=200)
    except:
        return Response(data={
            'error_code': 1
        }, status=410)


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
        }, status=200)

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
            }, status=200)
        except:
            return Response(data={
                'error_code': 1
            }, status=200)


@api_view(['POST'])
def close_room(request):
    roomnum = int(request.data['roomnum'])
    room = Room.objects.get(pk=roomnum)
    try:
        room.state = False
        room.save()
        return Response(data={
            'error_code': 0
        }, status=200)
    except:
        return Response(data={
            'error_code': 1
        }, status=200)


@api_view(['GET', 'POST'])
def interviewee_list(request):
    if request.method == 'GET':
        user = request.user
        room_list = Room.objects.filter(manager=user)
        interviewee_list = []
        for r in room_list:
            for i in r.interviewees.all():
                interviewee_list.append({
                    'num': i.id,
                    'username': i.username,
                    'email': i.email,
                    'telephone': i.telephone,
                    'address': i.addr,
                    'state': i.state
                })
        return Response(data={
            'interviewee_list': interviewee_list
        }, status=200)

    elif request.method == 'POST':
        post_data = {
            'num': int(request.data['num']),
            'username': request.data['username'],
            'email': request.data['email'],
            'telephone': request.data['telephone'],
            'address': request.data['address']
        }
        interviewee = Interviewee.objects.get(pk=post_data['num'])
        try:
            interviewee.username = post_data['username']
            interviewee.email = post_data['email']
            interviewee.telephone = post_data['telephone']
            interviewee.addr = post_data['address']
            interviewee.save()
            return Response(data={
                'error_code': 0
            }, status=200)
        except:
            return Response(data={
                'error_code': 1
            }, status=200)


def delete_interviewee(request):
    num = request.data['data']
    interviewee = Interviewee.objects.get(pk=num)
    try:
        interviewee.delete()
        return Response(data={
            'error_code': 0
        }, status=200)
    except:
        return Response(data={
            'error_code': 1
        }, status=200)


def add_interviewee(request):

    return
