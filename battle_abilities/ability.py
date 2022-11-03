from enum import Enum


class Range(Enum):
    SINGLE = 1,
    AREA = 2,


class Ability:
    def __init__(self, range_type: Range):
        self.range_type = range_type
