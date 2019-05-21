from django.shortcuts import render
from django.db import models
from django.http import HttpResponse

from .models import Link


# Create your views here.

def index(request):
    return HttpResponse("at index") 

def detail(request, Link_id):

    return HttpResponse("You're looking at link %s." % Link_id)
