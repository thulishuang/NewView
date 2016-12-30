from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import *
from Room.models import *
from NewView.settings import EMAIL_HOST, EMAIL_HOST_USER, \
    EMAIL_HOST_PASSWORD, SERVER_ADDR

# Use request.session['status'] to record user status
# Use request.session['username'] to record user name


@api_view(['GET', 'POST'])
def user_login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return Response(data={
               'error_code': 0
            }, status=200)
        else:
            return Response(data={
                'error_code': 1
            }, status=200)

    elif request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(data={
                'error_code': 0,
            }, status=200)
        else:
            return Response(data={
                'error_code': 1
            }, status=200)


@api_view(['POST'])
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response(data={
            'error_code': 0
        }, status=200)
    else:
        return Response(data={
            'error_code': 1
        }, status=200)

@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            index_table = IndexTable.objects.get(user_id=user.id)
            user_data = {
                'username': request.user.username,
                'room_num': index_table.own_room_num,
            }
            room_list = Room.objects.filter(manager=request.user)
            room_data = [
                {
                    'num': r.id,
                    'title': r.title,
                    'description': r.description,
                    'interviewer_email': r.interviewer_email,
                    'state': r.state
                } for r in room_list
            ]
            return Response(data={
                'user': user_data,
                'roomlist': room_data,
                'error_code': 0
            }, status=200)
        else:
            return Response(data={
                'error_code': 1,
                'error_data': 'no user log in'
            }, status=200)

    elif request.method == "POST":
        post_data = {
            'room_id': int(request.data['roomnum']),
            'title': request.data['title'],
            'description': request.data['description'],
            'interviewer_email': request.data['interviewer_email']
        }
        room = Room.objects.get(pk=post_data['room_id'])
        try:
            room.title = post_data['title']
            room.description = post_data['description']
            room.interviewer_email = post_data['interviewer_email']
            room.save()
            return Response(data={
                'error_code': 0
            }, status=200)
        except:
            return Response(data={
                'error_code': 1
            }, status=200)


@api_view(['POST'])
def change_room(request):
    room_id = int(request.data['roomnum'])
    room = Room.objects.get(id=room_id)
    try:
        room.state = not room.state
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
        index_table = IndexTable.objects.get(user_id=user.id)
        data_list = []
        for i in index_table.interviewee_list.all():
            data_list.append({
                'num': i.id,
                'username': i.username,
                'email': i.email,
                'telephone': i.telephone,
                'address': i.addr,
                'state': i.state
            })
        return Response(data={
            'interviewee_list': data_list
        }, status=200)

    elif request.method == 'POST':
        post_data = {
            'num': request.data['num'],
            'username': request.data['username'],
            'email': request.data['email'],
            'telephone': request.data['telephone'],
            'address': request.data['address']
        }
        try:
            interviewee = Interviewee.objects.get(pk=post_data['num'])
            interviewee.username = post_data['username']
            interviewee.email = post_data['email']
            interviewee.telephone = post_data['telephone']
            interviewee.addr = post_data['address']
            interviewee.save()
            return Response(data={
                'error_code': 0
            }, status=200)

        except Interviewee.DoesNotExist:
            user = request.user
            index_table = IndexTable.objects.get(user_id=user.id)
            interviewee = Interviewee(
                username=post_data['username'],
                email=post_data['email'],
                telephone=post_data['telephone'],
                addr=post_data['address']
            )
            interviewee.save();
            index_table.interviewee_list.add(interviewee)
            index_table.save()
            return Response(data={
                'error_code': 0
            }, status=200)

        except:
            return Response(data={
                'error_code': 1
            }, status=200)


@api_view((["POST"]))
def invite_interviewer(request):
    room = Room.objects.get(id=request.data['roomid'])
    receiver = room.interviewer_email
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = receiver
        msg['Subject'] = room.title + "的面试通知"
        body = room.description + "\n请点击链接\n\t http://" + \
               SERVER_ADDR + ":3000\#" + room.title + "\n\t 参与面试！"
        msg.attach(MIMEText(body, 'plain'))

        server = SMTP(EMAIL_HOST)
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.starttls()
        server.sendmail(EMAIL_HOST_USER, receiver, msg.as_string())
        server.quit()

        return Response(data={
            'error_code': 0,
        }, status=200)
    except:
        return Response(data={
            'error_code': 1,
        }, status=200)


@api_view(['POST'])
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


@api_view((['POST']))
def send_mail(request):
    try:
        user = Interviewee.objects.get(id=request.data['userid'])
        room = Room.objects.get(id=request.data['roomid'])
        receiver = user.email

        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = receiver
        msg['Subject'] = room.title + "的面试通知"
        body = room.description + "\n请点击链接\n\t http://" + \
               SERVER_ADDR + ":3000\#" + room.title + "\n\t 参与面试！"
        msg.attach(MIMEText(body, 'plain'))

        server = SMTP(EMAIL_HOST)
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.starttls()
        server.sendmail(EMAIL_HOST_USER, receiver, msg.as_string())
        server.quit()

        return Response(data={
            'error_code': 0
        }, status=200)
    except:
        return Response(data={
            'error_code': 1
        }, status=200)