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
    alltext = '' if alltext == "" else str(alltext)
    generate_count = request.POST['number']
    generate_count = 1 if generate_count == '' else int(generate_count)
    letters = "".join(
        list(map(str, (
            re.sub(r"[^a-zA-Z0-9-А-Яа-яёЁЇїІіЄєҐґ]+",
            ' ',
            alltext
        ))))
    )
        
    words = letters.split()
    number__of_words = len(words)
    values = ""

    # validate
    errors = []
    if alltext.lower().__contains__(' ну ') or alltext.lower().__contains__('ну,'):
        errors.append("Без 'ну'.")
    if not alltext.strip():
        errors.append("'Text' must contain at least 1 word.")
    if generate_count < 1:
        errors.append("'Number of words' can not be less than 1.")
    if number__of_words < generate_count:
        errors.append(
            "'Number of words' can not be greater than word count in the text.")
    if (len(errors) != 0):
        dto = RandomWordDto(alltext, generate_count, None)
        return __create_word_response(request, dto, errors)

    # generate
    values = random.sample(words, generate_count)

    # save
    timestamp = datetime.now(timezone.utc)
    wordSet = RandWordSet(
        user=None if request.user.is_anonymous else request.user,
        generated_at=timestamp,
        count=generate_count,
        all_text=alltext,
        values=values,
    )
    wordSet.save()

    dto = RandomWordDto(alltext, generate_count, values)
    return __create_word_response(request, dto, errors)
