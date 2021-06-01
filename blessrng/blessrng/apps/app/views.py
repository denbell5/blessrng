"""
Definition of views.
"""
from typing import Text
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render
from app.validators import *
import re

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def sign_up(request):
    
    if request.method == 'GET':
        username = None
        email = None
        password = None
        errors = []
        return __create_sign_up_responce(request, username, email, password, errors)
    elif request.method == 'POST':
        username = str(request.POST['username'])
        email = str(request.POST['email'])
        password = str(request.POST['password'])
        
    #validation
    errors = sign_up_validation_errors(email,password,username)
    if (User.objects.filter(username=username).exists()):
        errors.append('user allready exists')
    if (len(errors) != 0):
        return __create_sign_up_responce(request, username, email, password, errors)

    #save user 
    user = User.objects.create_user(username, email, password)

    return __create_sign_up_responce(request, username, email, password, errors)




def __create_sign_up_responce(request, username, email, password, errors):
    template = loader.get_template('app/sign_up.html')
    context = {'username': username,
               'email': email,
               'password': password,
               'errors' : errors}
    return HttpResponse(template.render(context, request))