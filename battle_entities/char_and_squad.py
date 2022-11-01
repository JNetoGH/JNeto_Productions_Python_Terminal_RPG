import enum
from ui.battle_stats import *


class Ownership(enum.Enum):
    NULL = -1,
    PLAYER = 0,
    ENEMY = 1


class Character:

    def __init__(self, name: str, health: int, mana: int, armor: int, weapon_dmg: int, initiative: int):
        self.name = name.capitalize()
        self.health = health
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative
        self.turn_order = 0
        self.ownership: Ownership = Ownership.NULL

    def is_dead(self) -> bool:
        return self.health <= 0

    def to_string(self) -> str:
        return get_char_card(self, GENERAL_CARD_LENGTH)


class Squad:

    def __init__(self, ownership: Ownership, squad_name: str, list_of_chars: list[Character]):
        self.squad_name = squad_name
        self.list_of_char = list_of_chars
        self.ownership = ownership
        self._set_chars_ownership_to_same_as_squad()

    def _set_chars_ownership_to_same_as_squad(self) -> None:
        for char in self.list_of_char:
            char.ownership = self.ownership

    def to_string(self) -> str:
        return get_squad_char_cards_inline(self, GENERAL_CARD_LENGTH, GENERAL_CARD_PADDING)