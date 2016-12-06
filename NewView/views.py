from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "home.html"
    version = "0.0.1"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'version': self.version})