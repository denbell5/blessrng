from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.data.random_generators.password_generators import generate_passwords
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone
# Create your views here.


def __create_integer_response(request: HttpRequest, dto: RandomIntDto, errors: List[str]):
    template = loader.get_template(Const.Http.RandInt.template_name)
    context = {
        RandomIntDto.Const.dto_name: dto,
        Const.Http.error_list_name: errors
    }
    return HttpResponse(template.render(context, request))


def integer(request: HttpRequest):
    if request.method == Const.Http.Methods.get:
        return __integer_get(request)
    elif request.method == Const.Http.Methods.post:
        return __integer_post(request)


def __integer_get(request: HttpRequest):
    dto = RandomIntDto(None, None, None, None)
    return __create_integer_response(request, dto, [])


def __integer_post(request: HttpRequest):
    timestamp = datetime.now(timezone.utc)

    # map
    count = request.POST[RandomIntDto.Const.count_name]
    count = RandomIntDto.Const.count_default if count == '' else int(count)
    floor = request.POST[RandomIntDto.Const.floor_name]
    floor = RandomIntDto.Const.floor_default if floor == '' else int(floor)
    ceiling = request.POST[RandomIntDto.Const.ceiling_name]
    ceiling = RandomIntDto.Const.ceiling_default if ceiling == '' else int(
        ceiling)

    # validate
    errors = []
    if (count < 1 or count > 100):
        errors.append("'Length' must be between 1 and 100 exclusive.")
    if (floor > ceiling):
        errors.append("'From' can not be greater than 'To'.")
    if (len(errors) != 0):
        dto = RandomIntDto(count, floor, ceiling, None)
        return __create_integer_response(request, dto, errors)

    # generate
    values = []
    for i in range(count):
        values.append(randint(floor, ceiling))

    # save
    intSet = RandIntSet(
        user=None if request.user.is_anonymous else request.user,
        generated_at=timestamp,
        count=count,
        floor=floor,
        ceiling=ceiling,
        values=values,
    )
    intSet.save()

    # respond
    dto = RandomIntDto(count, floor, ceiling, values)
    return __create_integer_response(request, dto, errors)


def password(request: HttpRequest):
    if request.method == Const.Http.Methods.get:
        return __password_get(request)
    elif request.method == Const.Http.Methods.post:
        return __password_post(request)


def __password_get(request: HttpRequest):
    dto = RandomPasswordDto(None, None, None)
    return __create_password_response(request, dto, [])


def __password_post(request: HttpRequest):
    # map
    password_length = request.POST['password_length']
    password_length = 10 if password_length == '' else int(password_length)
    password_count = request.POST['password_count']
    password_count = 1 if password_count == '' else int(password_count)
    passwords = generate_passwords(password_length, password_count)
    
    # validate
    errors = []
    if (password_count < 1 or password_count > 100):
        errors.append("'Count' must be between 1 and 100 exclusive.")
    if (password_length < 1):
        errors.append("Password can't have less than 1 character")
    if (len(errors) != 0):
        dto = RandomPasswordDto(password_length, passwords, password_count)
        return __create_password_response(request, dto, errors)


    
    dto = RandomPasswordDto(password_length, passwords, password_count)
    return __create_password_response(request, dto, [])


def __create_password_response(request: HttpRequest, dto: RandomIntDto, errors: List[str]):
    template = loader.get_template('generators/password.html')
    context = {
        'passwords_dto': dto,
        Const.Http.error_list_name: errors
    }
    return HttpResponse(template.render(context, request))
