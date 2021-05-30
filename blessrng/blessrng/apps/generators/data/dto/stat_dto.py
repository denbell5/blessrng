from typing import List
from datetime import datetime
from generators.models import *


class StatSetBaseDto:
    def __init__(self, type: str, generated_at: datetime):
        self.type = type
        self.generated_at: generated_at


class StatDto:  # dto for all statistics: latest 10 requests, total requests, total from anon etc.
    def __init__(self, latest: List[StatSetBaseDto]):
        self.latest = latest


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
