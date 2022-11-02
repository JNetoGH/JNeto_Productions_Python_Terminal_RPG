

class Spell:
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int):
        self.name = name
        self.description = description


class DmgSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int):
        super().__init__(name, description, effect_points, mana_cost)


class HealingSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int):
        super().__init__(name, description, effect_points, mana_cost)

