from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
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




def stat(request: HttpRequest):
    usr_id = request.user.id
    latest = get_latest_stats(usr_id)
    
    # get all stat and create StatDto from it
    int_gen_count = RandIntSet.objects.count() 
    pwd_gen_count = RandPwdSet.objects.count()
    word_gen_count = RandWordSet.objects.count()

    total_gen_count = int_gen_count + pwd_gen_count + word_gen_count
    
    anon_gen_count = RandIntSet.objects.filter(user_id = None).count() + RandPwdSet.objects.filter(user_id = None).count() + RandWordSet.objects.filter(user_id = None).count()
    registered_gen_count = total_gen_count - anon_gen_count

    registered_users = User.objects.count()
    avg_gen_per_user = registered_gen_count / registered_users

    site_stat_dto = SiteStatDto(int_gen_count, pwd_gen_count, word_gen_count, total_gen_count, anon_gen_count, registered_gen_count, registered_users, avg_gen_per_user)
    
    # get user stat 
    int_gen_count = RandIntSet.objects.filter(user_id = usr_id).count() 
    pwd_gen_count = RandPwdSet.objects.filter(user_id = usr_id).count()
    word_gen_count = RandWordSet.objects.filter(user_id = usr_id).count()
    total_gen_count = int_gen_count + pwd_gen_count + word_gen_count
    user_stat_dto = UserStatDto(int_gen_count, pwd_gen_count, word_gen_count, total_gen_count, usr_id)
    
    # get random user entry
    entries = RandIntSet.objects.filter(user_id = usr_id)
    entries_list = list(entries)
    entries = RandPwdSet.objects.filter(user_id = usr_id)
    entries_list += list(entries)
    entries = RandWordSet.objects.filter(user_id = usr_id)
    entries_list += list(entries)
    random_entry = random.choice(entries_list) if entries_list else []
    if (type(random_entry) is RandIntSet) :
        random_entry_dto = map_int_to_stat_dto(random_entry)
    elif (type(random_entry) is RandPwdSet) :
        random_entry_dto = map_pwd_to_stat_dto(random_entry)
    elif (type(random_entry) is RandWordSet) :
        random_entry_dto = map_word_to_stat_dto(random_entry)
    else:
        random_entry_dto = None
    
    dto = StatDto(site_stat = site_stat_dto, user_stat = user_stat_dto, latest=latest, random_entry = random_entry_dto)
    
    return __create_stat_response(request, dto)


def __create_stat_response(request: HttpRequest, dto: StatDto):
    template = loader.get_template('generators/stat.html')
    context = {'dto': dto}
    return HttpResponse(template.render(context, request))