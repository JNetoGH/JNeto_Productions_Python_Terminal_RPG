from enum import Enum
from typing import Union
from battle_entities.char_and_squad import Character, Squad


class KindOfAction(Enum):
    PHYSICAL_DMG = 1
    SPELL = 2


class Action:

    class _ActionRange(Enum):
        SINGLE = 1,
        AREA = 2

    #  Can receive both a Char or Squad, I cant use overload in Python, so that's what I came up with
    #  it will check internally what has been passed
    def __init__(self, current_char: Character, char_or_squad_target: Union[Character, Squad], kind_of_action: KindOfAction, spell = None):

        # the amount of points an action has dealt, dmg, cure etc
        self.dmg_dealt = 0
        self.healing_dealt = 0
        self.armor_bonus_dealt = 0

        # gets if it's a single range action (char -> char) or a area range action (char -> squad)
        action_range = None
        if isinstance(char_or_squad_target, Character):
            action_range = Action._ActionRange.SINGLE
        elif isinstance(char_or_squad_target, Squad):
            action_range = Action._ActionRange.AREA

        # makes the action occur
        if kind_of_action == KindOfAction.PHYSICAL_DMG:
            if action_range == Action._ActionRange.SINGLE:
                self.dmg_dealt = Action._physical_atk(current_char, char_or_squad_target)
            elif action_range == Action._ActionRange.AREA:
                for target_char in char_or_squad_target.list_of_char:
                    if not (target_char.is_dead()):
                        self.dmg_dealt = Action._physical_atk(current_char, target_char)
        elif kind_of_action == KindOfAction.SPELL:
            if action_range == Action._ActionRange.SINGLE:
                pass
            elif action_range == Action._ActionRange.AREA:
                pass

    @staticmethod
    def _physical_atk(charAtk: Character, charDef: Character) -> int:  # used in_player_action() and _ai_cation()
        dmg: int = charAtk.weapon_dmg - charDef.armor
        if dmg < 0:
            dmg = 0
        charDef.health -= dmg
        return dmg
