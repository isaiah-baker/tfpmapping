from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from view.models import Link


from .models import Link

# Create your views here.
def index(request):
    id = User.id
    link_list = Link.objects.order_by('-pub_date')  
    context = {'link_list': link_list}

    return render(request, 'view/view.html', context)
