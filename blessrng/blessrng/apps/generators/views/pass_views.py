from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from generators.data.dto.dto import *
from generators.data.random_generators.password_generators import generate_passwords
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone


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
    
    
    # validate
    passwords = []
    errors = []
    if (password_count < 1 or password_count >= 64):
        errors.append("'Count' must be between 1 and 64 exclusive.")
    if (password_length < 1):
        errors.append("Password can't have less than 1 character")
    if (len(errors) != 0):
        dto = RandomPasswordDto(password_length, passwords, password_count)
        return __create_password_response(request, dto, errors)

    # generate
    passwords = generate_passwords(password_length, password_count)
    
    # save
    timestamp = datetime.now(timezone.utc)
    pwdSet = RandPwdSet(
        user=None if request.user.is_anonymous else request.user,
        generated_at=timestamp,
        count= password_count,
        pwd_length=password_length,
        values=passwords,
    )
    pwdSet.save()

    # respond    
    dto = RandomPasswordDto(password_length, passwords, password_count)
    return __create_password_response(request, dto, [])


def __create_password_response(request: HttpRequest, dto: RandomIntDto, errors: List[str]):
    template = loader.get_template('generators/password.html')
    context = {
        'passwords_dto': dto,
        Const.Http.error_list_name: errors
    }
    return HttpResponse(template.render(context, request))