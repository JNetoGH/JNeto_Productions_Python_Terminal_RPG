from enum import Enum
from battle_abilities.ability import Range, Ability


class Spell(Ability):
    class SpellRange(Enum):
        SINGLE = 1,
        AREA = 2

    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int, range_type: Range, can_affect_caster: bool):
        super().__init__(range_type, can_affect_caster)
        self.mana_cost = mana_cost
        self.effect_points = effect_points
        self.name = name
        self.description = description


class DmgSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int, range_type: Range, can_affect_caster: bool):
        super().__init__(name, description, effect_points, mana_cost, range_type, can_affect_caster)


class HealingSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int, range_type: Range, can_affect_caster: bool):
        super().__init__(name, description, effect_points, mana_cost, range_type, can_affect_caster)

