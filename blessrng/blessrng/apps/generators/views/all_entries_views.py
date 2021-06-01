
from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader 
from django.core.paginator import Paginator
import random
from generators.data.dto.dto import *
from generators.data.random_generators.stat_generators import *
from generators.data.mappings.int_mapper import *
from generators.data.mappings.pwd_mapper import *
from generators.data.mappings.word_mapper import *
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone
from generators.data.dto.stat_dto import *




def all_entries(request: HttpRequest):

    # get all user entries
    current_page = request.GET['page'] if 'page' in request.GET else 1
    user_id = request.user.id
    all_entries = get_all_user_entries(user_id)
    p = Paginator(all_entries, 5)
    dto = AllEntriesDto(p.page(current_page).object_list)
    return __create_all_entries_response(request, dto, p.page(current_page))


def __create_all_entries_response(request: HttpRequest, dto, page_obj):
    template = loader.get_template('generators/all_entries.html')
    context = {'dto': dto , 
               'page_obj': page_obj}
    return HttpResponse(template.render(context, request))