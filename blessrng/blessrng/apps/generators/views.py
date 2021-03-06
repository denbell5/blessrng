from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.data.random_generators.password_generators import generate_password
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone
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
    dto = RandomIntDto(None, None, None, None)
    return __create_integer_response(request, dto)


def __integer_post(request: HttpRequest):
    timestamp = datetime.now(timezone.utc)

    count = request.POST[RandomIntDto.Const.count_name]
    count = RandomIntDto.Const.count_default if count == '' else int(count)
    floor = request.POST[RandomIntDto.Const.floor_name]
    floor = RandomIntDto.Const.floor_default if floor == '' else int(floor)
    ceiling = request.POST[RandomIntDto.Const.ceiling_name]
    ceiling = RandomIntDto.Const.ceiling_default if ceiling == '' else int(
        ceiling)

    values = []
    for i in range(count):
        values.append(randint(floor, ceiling))

    intSet = RandIntSet(
        user=None if request.user.is_anonymous else request.user,
        generated_at=timestamp,
        count=count,
        floor=floor,
        ceiling=ceiling,
        values=values,
    )
    intSet.save()

    dto = RandomIntDto(count, floor, ceiling, values)
    return __create_integer_response(request, dto)


def generate_pass(request):
    password_length = int(request.POST['password_length'])
    password = generate_password(password_length)
    dto = RandomPasswordDto(password_length, password)
    template = loader.get_template('generators/index.html')
    context = {'password_dto': dto}
    return HttpResponse(template.render(context, request))
