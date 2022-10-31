from ui.battle_stats import *


class Character:

    def __init__(self, name: str, health: int, mana: int, armor: int, weapon_dmg: int, initiative: int):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative
        self.turn_order = 0

    def is_dead(self) -> bool:
        return self.health <= 0

    def to_string(self) -> str:
        return get_char_card(self, GENERAL_LINE_LENGTH)


class Squad:

    def __init__(self, squad_name: str, list_of_chars: list[Character]):
        self.squad_name = squad_name
        self.list_of_char = list_of_chars

    def to_string(self) -> str:
        return get_squad_char_cards_inline(self, GENERAL_LINE_LENGTH)