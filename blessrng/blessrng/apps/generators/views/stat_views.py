from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone
from generators.data.dto.stat_dto import *


def __create_stat_response(request: HttpRequest, dto: StatDto):
    template = loader.get_template('generators/stat.html')
    context = {'dto': dto}
    return HttpResponse(template.render(context, request))


def stat(request: HttpRequest):
    # get all stat and create StatDto from it
    dto = StatDto(latest=[])
    return __create_stat_response(request, dto)
