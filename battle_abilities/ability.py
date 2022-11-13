class Ability:
    def __init__(self, can_affect_allies: bool, can_affect_caster: bool):
        self.can_affect_caster = can_affect_caster
        self.can_affect_allies = can_affect_allies

    def exec(self, caster, target):
        pass


class PhysicalAtk(Ability):
    def __init__(self):
        super().__init__(can_affect_allies=False, can_affect_caster=False)
        self.dmg = 0

    def exec(self, caster, target):
        dmg = caster.weapon_dmg - target.armor
        if dmg < 0:
            dmg = 0
        target.health -= dmg
        if target.health < 0:
            target.health = 0
        self.dmg = dmg


class Spell(Ability):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int,  can_affect_allies: bool, can_affect_caster: bool):
        super().__init__(can_affect_allies=can_affect_allies, can_affect_caster=can_affect_caster)
        self.mana_cost = mana_cost
        self.effect_points = effect_points
        self.name = name
        self.description = description

    def decrease_mana_from_caster(self, charCaster):
        charCaster.mana -= self.mana_cost

    def exec(self, caster, target):
        self.decrease_mana_from_caster(caster)


class DmgSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int):
        super().__init__(name, description, effect_points, mana_cost, False, False)

    def exec(self, caster, target):
        super(DmgSpell, self).exec(caster, target)
        target.health -= self.effect_points
        if target.health < 0:
            target.health = 0

class HealingSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int, can_affect_allies: bool, can_affect_caster: bool):
        super().__init__(name, description, effect_points, mana_cost, can_affect_allies=can_affect_allies, can_affect_caster=can_affect_caster)

    def exec(self, caster, target):
        super(HealingSpell, self).exec(caster, target)
        target.health += self.effect_points
