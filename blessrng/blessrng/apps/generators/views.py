from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.data.random_generators.password_generators import generate_password
from generators.models import *
from generators.data.constants.constants import Const
# Create your views here.


def __create_integer_response(request: HttpRequest, dto: RandomIntDto):
    template = loader.get_template(Const.Http.RandInt.template_name)
    context = {RandomIntDto.Const.dto_name: dto}
    return HttpResponse(template.render(context, request))


def integer(request: HttpRequest):
    if request.method == Const.Http.Methods.get:
        return __integer_get(request)
    elif request.method == Const.Http.Methods.post:
        return __integer_post(request)


def __integer_get(request: HttpRequest):
    dto = RandomIntDto(1, None, None, None)
    return __create_integer_response(request, dto)


def __integer_post(request: HttpRequest):
    count = int(request.POST[RandomIntDto.Const.count_name])
    floor = int(request.POST[RandomIntDto.Const.floor_name])
    ceiling = int(request.POST[RandomIntDto.Const.ceiling_name])
    values = []
    for i in range(count):
        values.append(randint(floor, ceiling))
    dto = RandomIntDto(count, floor, ceiling, values)
    return __create_integer_response(request, dto)


def generate_pass(request):
    password_length = int(request.POST['password_length'])
    password = generate_password(password_length)
    dto = RandomPasswordDto(password_length, password)
    template = loader.get_template('generators/index.html')
    context = {'password_dto': dto}
    return HttpResponse(template.render(context, request))
