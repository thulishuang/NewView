from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import Manager
from Room.models import Room


class AccountLogin(View):
    template_name = "a/login.html"

    def get(self, request, *args, **kwargs):
        if 'login_Status' in request.session and request.session['login_status']:
            return HttpResponseRedirect('/account/detail')
        return render(request, self.template_name, {'msg': ''})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        try:
            Manager.objects.get(username=username, password=password)
            request.session['login_status'] = True
            request.session['username'] = username
            return HttpResponseRedirect('/account/detail')

        except Manager.DoesNotExist:
            return render(request, self.template_name, {'msg': "invalid username or password"})


class AccountLogout(View):
    template_name = 'a/logout.html'

    def get(self, request, *args, **kwargs):
        if 'login_status' not in request.session or not request.session['login_status']:
            return HttpResponseRedirect('/account/login')
        request.session['login_status'] = False
        return render(request, self.template_name)


class AccountDetail(View):
    template_name = 'a/detail.html'

    def get(self, request):
        if 'login_status' not in request.session or not request.session['login_status']:
            return HttpResponseRedirect('/account/login')

        current_user = Manager.objects.get(username=request.session['username'])
        userinfo = {
            'username': current_user.username,
        }
        return render(request, self.template_name)

class EditRoom(View):
    template_name = 'a/editroom.html'

    def get(self, request):
        return

    def post(self, request):
        return
