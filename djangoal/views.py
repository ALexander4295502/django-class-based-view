from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'home.html'


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World")
