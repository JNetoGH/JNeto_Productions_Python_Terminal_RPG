from battle_abilities.ability import Ability, Range


class PhysicalAtk(Ability):
    def __init__(self):
        super().__init__(Range.SINGLE, can_affect_caster=False)
