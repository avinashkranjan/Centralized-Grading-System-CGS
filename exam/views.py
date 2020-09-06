from django.shortcuts import render
from django.shortcuts import HttpResponse


def dashboard(request):
    return HttpResponse('Dashboard')
