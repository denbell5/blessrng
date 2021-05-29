from typing import List

from django.http.request import HttpRequest


class RandomIntDto:
    class Const:
        dto_name = 'random_int_dto'
        count_name = 'count'
        floor_name = 'floor'
        ceiling_name = 'ceiling'
        value_name = 'value'
        count_default = 1
        floor_default = 1
        ceiling_default = 322

    def __init__(self, count: int, floor: int, ceiling: int, values: List[int]):
        self.count = count
        self.floor = floor
        self.ceiling = ceiling
        self.values = values


class RandomPasswordDto:
    def __init__(self, length, passwords, count):
        self.length = length
        self.passwords = passwords
        self.count = count