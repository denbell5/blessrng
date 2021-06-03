"""
Definition of views.
"""

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from app.validators import *


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

    # validation
    errors = sign_up_validation_errors(email, password, username)
    if (User.objects.filter(username=username).exists()):
        errors.append('user allready exists')
    if (len(errors) != 0):
        return __create_sign_up_responce(request, username, email, password, errors)

    # save user
    user = User.objects.create_user(username, email, password)

    return __create_sign_up_responce(request, username, email, password, errors)


def __create_sign_up_responce(request, username, email, password, errors):
    template = loader.get_template('app/sign_up.html')
    context = {'username': username,
               'email': email,
               'password': password,
               'errors': errors}
    return HttpResponse(template.render(context, request))
