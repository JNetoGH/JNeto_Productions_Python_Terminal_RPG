import os

import ui.battle_stats
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_phases.initiative_phase import InitiativePhase


class ActionPhase:
    def __init__(self, initiative_phase: InitiativePhase):
        self.initiative_phase = initiative_phase
        self.squad1 = self.initiative_phase.squad1
        self.squad2 = self.initiative_phase.squad2
        # used for action order control: char will be removed if dead o if has already played
        self.action_order_list: list[Character] = self.initiative_phase.action_order_list
        # used for combat: chars will not be removed
        self.all_chars = self.action_order_list.copy()

        self.force_skip = False
        while len(self.action_order_list) != 0:  # while action_order_list is not empty
            current_char = self.action_order_list[0]
            self._run_action_turn(current_char)
            if self.force_skip:
                self.force_skip = False
                break
            self.remove_a_char_from_action_order_list(current_char)
            self.remove_dead_chars_from_action_order_list()
            os.system("cls")
            print()

            print(ui.battle_stats.get_battle_current_state(self.initiative_phase), end="")

        if self.is_there_a_winner() == Ownership.PLAYER:
            print("player venceu")
        elif self.is_there_a_winner() == Ownership.ENEMY:
            print("enemy venceu")
        elif self.is_there_a_winner() == Ownership.NULL:
            print("action_order_list is empty")

    def _run_action_turn(self, char: Character):
        if char.ownership == Ownership.PLAYER:
            self._player_action(char)
        elif char.ownership == Ownership.ENEMY:
            self._ai_action()
        print()  # jumps a line

    def _player_action(self, current_char: Character):

        # prints the current char
        print(f"\nTURN: {current_char.name}")
        print(ui.battle_stats.get_char_card(current_char))

        # picks an alive char only
        other_char: Character = None
        while other_char is None:

            chosen_char_name = input(f"Which char should {current_char.name} pick?: ").capitalize()
            if chosen_char_name == "Quit":
                self.force_skip = True
                return

            for char in self.all_chars:
                if char.name.capitalize() == chosen_char_name:
                    other_char = char

            if other_char is None:
                print(f"invalid input, {chosen_char_name} does not exist")
            elif other_char is current_char:
                print("invalid input, a char can't atk itself")
                other_char = None
            elif other_char.is_dead():
                print(f"invalid input, {other_char.name} is already dead")
                other_char = None

        # makes the atk and remove the char if its dead
        dmg = ActionPhase._physical_atk(current_char, other_char)

        # prints battle current state
        print(f"{current_char.name} attacked {other_char.name}: tot dmg = {dmg}")
        print()

    @staticmethod
    def _physical_atk(charAtk: Character, charDef: Character):  # used in_player_action() and _ai_cation()
        dmg: int = charAtk.weapon_dmg - charDef.armor
        if dmg < 0:
            dmg = 0
        charDef.health -= dmg
        return dmg

    def _ai_action(self):
        print("\nai action no implemented yet, using same system as player")
        self._player_action()
        input("press any key to continue")

    def remove_a_char_from_action_order_list(self, char: Character) -> bool:
        if char in self.action_order_list:
            self.action_order_list.remove(char)
            return True

    def remove_dead_chars_from_action_order_list(self) -> bool:
        for char in self.action_order_list:
            if char.is_dead():
                self.action_order_list.remove(char)
                return True

    def is_there_a_winner(self) -> Ownership:
        if ActionPhase._is_squad_all_dead(self.squad1):
            return self.squad2.ownership
        elif ActionPhase._is_squad_all_dead(self.squad2):
            return self.squad1.ownership
        return Ownership.NULL

    @staticmethod
    def _is_squad_all_dead(squad: Squad):  # used in is_there_a_winner()
        is_squad_all_dead = True
        for char in squad.list_of_char:
            if not (char.is_dead()):
                is_squad_all_dead = False
        return is_squad_all_dead
