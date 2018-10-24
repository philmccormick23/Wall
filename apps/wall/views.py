from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import *


def index(request):
    dictionary = {
        'users' :  User.objects.all()
    }
    #for u in User.objects.all():
        #u.delete()
    
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        u= User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['id']=u.id
        request.session['first_name']=u.first_name
        return redirect('/success')

def login(request):
    users = User.objects.all()
    for thing in users: 
        if request.POST['email'] == thing.email and request.POST['password'] == thing.password:
            u=User.objects.get(email=request.POST['email'])
            request.session['id']=u.id
            request.session['first_name']=u.first_name
    return redirect('/success')

def success(request):
    dictionary  = {
        'messages' : Message.objects.all(),
        'comments' : Comment.objects.all()
    }
    return render(request,'success.html', dictionary)

def message(request):
    Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['id']))
    return redirect('/success')

def comment(request):
    Comment.objects.create(comment=request.POST['comment'], message=Message.objects.get(id=request.POST['message']), user=User.objects.get(id=request.session['id'])) 
    return  redirect('/success')