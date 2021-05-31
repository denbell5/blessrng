from typing import List
from generators.data.dto.stat_dto import *
from generators.data.mappings.int_mapper import *
from generators.data.mappings.pwd_mapper import *
from generators.data.mappings.word_mapper import *
from generators.models import *


def get_latest_stats():
    ints = RandIntSet.objects.order_by('-generated_at')[:10]
    pwds = RandPwdSet.objects.order_by('-generated_at')[:10]
    wrds = RandWordSet.objects.order_by('-generated_at')[:10]
    int_dtos = list(map(lambda obj: map_int_to_stat_dto(obj), ints))
    pwd_dtos = list(map(lambda obj: map_pwd_to_stat_dto(obj), pwds))
    word_dtos = list(map(lambda obj: map_word_to_stat_dto(obj), wrds))
    joined: List[StatSetBaseDto] = int_dtos + pwd_dtos + word_dtos
    joined.sort(key=lambda obj: obj.generated_at, reverse=1)
    return joined[:10]


def get_all_user_entries(user_id):
    ints = RandIntSet.objects.filter(user_id = user_id)
    pwds = RandPwdSet.objects.filter(user_id = user_id)
    wrds = RandWordSet.objects.filter(user_id = user_id)
    int_dtos = list(map(lambda obj: map_int_to_stat_dto(obj), ints))
    pwd_dtos = list(map(lambda obj: map_pwd_to_stat_dto(obj), pwds))
    word_dtos = list(map(lambda obj: map_word_to_stat_dto(obj), wrds))
    joined: List[StatSetBaseDto] = int_dtos + pwd_dtos + word_dtos
    joined.sort(key=lambda obj: obj.generated_at, reverse=1)
    return joined