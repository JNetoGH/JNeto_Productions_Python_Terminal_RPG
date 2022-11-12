from enum import Enum


class Range(Enum):
    SINGLE = 1,
    AREA = 2,


class Ability:
    def __init__(self, range_type: Range, can_affect_caster: bool):
        self.range_type = range_type
        self.can_affect_caster = can_affect_caster
