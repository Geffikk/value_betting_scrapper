from django.shortcuts import render
from django.http import HttpResponse

from scripts.offices.Pinnacle import Pinnacle


def index(request):
    return render(request, "main.html")