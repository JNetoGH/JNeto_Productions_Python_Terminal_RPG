from battle_abilities.ability import Ability, Range


class PhysicalAtk(Ability):
    def __init__(self, range_type: Range):
        super().__init__(range_type)
