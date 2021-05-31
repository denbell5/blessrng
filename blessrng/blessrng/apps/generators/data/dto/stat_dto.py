from typing import List
from datetime import datetime
from generators.models import *


class StatSetBaseDto:
    def __init__(self, type: str, generated_at: datetime):
        self.type = type
        self.generated_at: generated_at


class StatDto:  # dto for all statistics: latest 10 requests, total requests, total from anon etc.
    def __init__(self, latest: List[StatSetBaseDto],site_stat, user_stat, random_entry):
        self.latest = latest
        self.site_stat = site_stat
        self.user_stat = user_stat

class SiteStatDto:
    def __init__(self, int_gen_count,
                 pwd_gen_count,
                 word_gen_count,
                 total_gen_count,
                 anon_gen_count,
                 registered_gen_count,
                 registered_users,
                 avg_gen_per_user):
        
        self.int_gen_count = int_gen_count
        self.pwd_gen_count = pwd_gen_count
        self.word_gen_count = word_gen_count

        self.total_gen_count = total_gen_count

        self.anon_gen_count = anon_gen_count
        self.registered_gen_count = registered_gen_count
        self.registered_users = registered_users
        self.avg_gen_per_user = avg_gen_per_user

class UserStatDto:
    def __init__(self, int_gen_count,
                 pwd_gen_count,
                 word_gen_count,
                 total_gen_count):
        self.int_gen_count = int_gen_count
        self.pwd_gen_count = pwd_gen_count
        self.word_gen_count = word_gen_count
        self.total_gen_count = total_gen_count


class IntStatDto(StatSetBaseDto):
    def __init__(
        self,
        type: str,
        generated_at: datetime,
        count: int,
        floor: int,
        ceiling: int,
        values: List[int]
    ):
        self.type = type
        self.generated_at = generated_at
        self.count = count
        self.floor = floor
        self.ceiling = ceiling
        self.values = values


class PwdStatDto(StatSetBaseDto):
    def __init__(
        self,
        type: str,
        generated_at: datetime,
        length, passwords, count
    ):
        self.type = type
        self.generated_at = generated_at
        self.length = length
        self.passwords = passwords
        self.count = count


class WordStatDto(StatSetBaseDto):
    def __init__(
        self,
        type: str,
        generated_at: datetime,
        alltext: str,
        values: List[str]
    ):
        self.type = type
        self.generated_at = generated_at
        self.alltext = alltext
        self.values = values