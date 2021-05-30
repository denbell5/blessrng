from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from random import randint
from generators.data.dto.dto import *
from generators.data.random_generators.stat_generators import *
from generators.models import *
from generators.data.constants.constants import Const
from datetime import datetime, timezone
from generators.data.dto.stat_dto import *




def stat(request: HttpRequest):
    # get all stat and create StatDto from it
    latest = get_latest_stats()

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
    usr_id = request.user.id
    int_gen_count = RandIntSet.objects.filter(user_id = usr_id).count() 
    pwd_gen_count = RandPwdSet.objects.filter(user_id = usr_id).count()
    word_gen_count = RandWordSet.objects.filter(user_id = usr_id).count()
    total_gen_count = int_gen_count + pwd_gen_count + word_gen_count
    user_stat_dto = UserStatDto(int_gen_count, pwd_gen_count, word_gen_count, total_gen_count)

    dto = StatDto(siteStat = site_stat_dto, userStat = user_stat_dto, latest=latest)
    
    return __create_stat_response(request, dto)


def __create_stat_response(request: HttpRequest, dto: StatDto):
    template = loader.get_template('generators/stat.html')
    context = {'dto': dto}
    return HttpResponse(template.render(context, request))