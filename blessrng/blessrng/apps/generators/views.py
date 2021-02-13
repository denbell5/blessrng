from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.data.random_generators.password_generators import generate_password
from generators.models import *
# Create your views here.


def _get_randint_response(request, dto: RandomIntDto):
    template = loader.get_template('generators/integer.html')
    context = {'random_int_dto': dto}
    return HttpResponse(template.render(context, request))


def integer(request):
    if request.method == 'GET':
        return __integer_get(request)
    elif request.method == 'POST':
        return __integer_post(request)


def __integer_get(request):
    dto = RandomIntDto(None, None, None)
    return _get_randint_response(request, dto)


def __integer_post(request):
    floor = int(request.POST['floor'])
    ceiling = int(request.POST['ceiling'])
    value = randint(floor, ceiling)
    dto = RandomIntDto(floor, ceiling, value)
    return _get_randint_response(request, dto)


def generate_pass(request):
    password_length = int(request.POST['password_length'])
    password = generate_password(password_length)
    dto = RandomPasswordDto(password_length, password)
    template = loader.get_template('generators/index.html')
    context = {'password_dto': dto}
    return HttpResponse(template.render(context, request))
