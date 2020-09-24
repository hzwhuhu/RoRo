from django.shortcuts import render
from django.http import HttpResponse
from RoRo import settings


def User(request):
    return render(request,'RoRo/base.html')
