from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import RandomWordDto
from generators.models import *
from generators.data.constants.constants import Const
import random
import re
from typing import List, ValuesView
from datetime import datetime, timezone


def text(request: HttpRequest):
    if request.method == Const.Http.Methods.get:
        return __word_get(request)
    elif request.method == Const.Http.Methods.post:
        return __word_post(request)


def __word_get(request: HttpRequest):
    dto = RandomWordDto(None, None, None)
    return __create_word_response(request, dto, [])


def __create_word_response(request: HttpRequest, dto: RandomWordDto, errors: List[str]):
    template = loader.get_template('generators/word.html')
    context = {
        'word_dto': dto,
        Const.Http.error_list_name: errors
    }
    return HttpResponse(template.render(context, request))


def __word_post(request):
    # map

    alltext = request.POST['alltext']
    alltext = ' ' if alltext == "" else str(alltext)
    number = request.POST['number']
    number = 1 if number == '' else int(number)
    leters = "".join(list(
        map(str, (re.sub(r"[^a-zA-Z0-9-А-Яа-яёЁЇїІіЄєҐґ]+", ' ', alltext)))))
    words = leters.split()
    number__of_words = len(words)
    value = ""
    # validator
    errors = []
    if number == 1 and alltext == ' ':
        errors.append("Please input some words")
        dto = RandomWordDto(alltext, number, value)
        return __create_word_response(request, dto, errors)
    if number < 0 or number == 0:
        errors.append(
            'You need to input only positive numbers bigger than 0 !')
        dto = RandomWordDto(alltext, number, value)
        return __create_word_response(request, dto, errors)
    if number__of_words >= number:
        value = random.sample(words, number)
        dto = RandomWordDto(alltext, number, value)
        return __create_word_response(request, dto, errors)
    if number__of_words <= number:
        errors.append('Error you need to input correct number of words!')
        dto = RandomWordDto(alltext, number, value)
        return __create_word_response(request, dto, errors)
    if (len(errors) != 0):
        dto = RandomWordDto(alltext, number, value, None)
        return __create_word_response(request, dto, errors)

    # save
    timestamp = datetime.now(timezone.utc)
    wordSet = RandWordSet(
        user=None if request.user.is_anonymous else request.user,
        generated_at=timestamp,
        alltext=alltext,
        number=number,
        value=value,
    )
    wordSet.save()
    dto = RandomWordDto(alltext, number, value)
    return __create_word_response(request, dto, errors)
