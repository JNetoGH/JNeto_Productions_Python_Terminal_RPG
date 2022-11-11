from ui import ui_resources, battle_stats
from typing import Union
from battle_abilities.ability import Range
from battle_abilities.physical_atk import PhysicalAtk
from battle_abilities.spells import Spell, DmgSpell, HealingSpell
from battle_core.action import Action
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.initiative_phase import InitiativePhase


class ActionPhase:

    def __init__(self, initiative_phase: InitiativePhase):
        self.initiative_phase = initiative_phase
        self.squad1 = self.initiative_phase.squad1
        self.squad2 = self.initiative_phase.squad2
        self.action_order_list: list[Character] = self.initiative_phase.action_order_list                               # used for action order control: char will be removed if dead or if has already played
        self._all_chars = self.action_order_list.copy()                                                                 # used for combat: chars will not be removed

        self._force_skip_turn = False
        self.force_quit_battle = False

        while len(self.action_order_list) != 0 and self.is_there_a_winner() == Ownership.NULL:                          # while action_order_list is not empty and there is no winner
            print(battle_stats.get_battle_current_state(self.initiative_phase), end="")                              # prints Ui
            current_char = self.action_order_list[0]                                                                    # sets the current char according to the action order list
            self._run_action_turn_for_char(current_char)                                                                # runs action of the current char user/AI based
            self.remove_a_char_from_action_order_list(current_char)                                                     # removes from the action order list the current char, passing the action to the next on if the is any
            self.remove_dead_chars_from_action_order_list()                                                             # removes all dead chars from the action order list th
            if self._force_skip_turn:                                                                                   # ActionPhase flow control: checks for skips and breaks, if there is none, cleans the screen to next char, if there is any
                self._force_skip_turn = False
                ui_resources.clear_terminal()
                print()
                continue
            elif self.force_quit_battle:
                ui_resources.clear_terminal()
                break
            else:
                input("press enter to next turn")
            ui_resources.clear_terminal()                                                                                            # clears the screen for the next ui
            print()

    def _run_action_turn_for_char(self, char: Character) -> None:
        if char.ownership == Ownership.PLAYER:
            self._player_action(char)
        elif char.ownership == Ownership.ENEMY:
            self._ai_action(char)
        print()  # jumps a line

    def _player_action(self, current_char: Character) -> None:

        print(f"\nTURN: {current_char.name}")
        print(battle_stats.get_char_card(current_char))  # prints the current char card

        action_done = False
        while not action_done:

            action_kind = input(f"What should {current_char.name} do? [1:Atk] [2:Spell] [3:Skip] [4:Quit]: ")

            if action_kind.capitalize() == "Atk" or action_kind == "1":                                                 # todo por return igual o do spell
                target_char: Character = self._get_a_target_by_name_from_player(current_char, can_pick_itself=False)
                action = Action(current_char, target_char, PhysicalAtk(Range.SINGLE))
                dmg = action.dmg_dealt
                print(f"{current_char.name} attacked {target_char.name}: tot dmg = {dmg}\n")
                action_done = True

            elif action_kind.capitalize() == "Spell" or action_kind == "2":
                spell = ActionPhase._get_a_valid_spell_in_char_from_player_or_return_code(current_char)
                if isinstance(spell, Spell):  # in case the player has chosen return spell won't be a Spell, will be -1
                    try:
                        target_char = self._get_a_target_by_name_from_player(current_char, can_pick_itself=isinstance(spell, HealingSpell))
                        action = Action(current_char, target_char, spell)
                        action_done = True
                    except:
                        print(f"{current_char.name} doesn't have enough mana ({current_char.mana}) to cast "
                              f"{spell.name} (cost:{spell.mana_cost})")

            elif action_kind.capitalize() == "Skip" or action_kind == "3":
                self._force_skip_turn = True
                action_done = True

            elif action_kind.capitalize() == "Quit" or action_kind == "4":
                self.force_quit_battle = True
                action_done = True

    @staticmethod
    def _get_a_valid_spell_in_char_from_player_or_return_code(current_char: Character) -> Union[Spell, int]:
        if not current_char.have_spells():
            print(f"invalid, {current_char.name} doesn't have any spells")
        else:
            ActionPhase._display_char_spells(current_char)
            while True:  # gets a valid spell asking its index
                spell_input = input("insert a spell number or type return to choose another action: ")
                if spell_input.capitalize() == "Return":
                    return -1
                elif not (spell_input.isnumeric()):
                    print("invalid input, please insert a index")
                elif spell_input.isnumeric():
                    spell_index = int(spell_input)
                    if 0 <= spell_index < len(current_char.spells):
                        return current_char.spells[spell_index]
                    else:
                        print(f"invalid input, there is no spell with index {spell_input}")

    @staticmethod  # todo mover isto para class que cuida das
    def _display_char_spells(current_char: Character) -> None:
        print(f"\n{current_char.name} Spells")
        print("--------------------------------------")
        count = 0
        for spell in current_char.spells:
            print(f"[{count}]{spell.name} (mana:{spell.mana_cost}): {spell.description}")
            count += 1
        print("--------------------------------------")

    def _get_a_target_by_name_from_player(self, current_char: Character, can_pick_itself: bool) -> Character:
        target_char: Character = None
        while target_char is None:
            chosen_char_name = input(f"Which char should {current_char.name} pick?: ").capitalize()
            for char in self._all_chars:
                if char.name.capitalize() == chosen_char_name:
                    target_char = char
            if target_char is None:
                print(f"invalid input, {chosen_char_name} does not exist")
            elif target_char is current_char and not(can_pick_itself):
                print("invalid input, a char can't atk itself")
                target_char = None
            elif target_char.is_dead():
                print(f"invalid input, {target_char.name} is already dead")
                target_char = None
        return target_char

    def _ai_action(self, char: Character) -> None:
        print("\nai action no implemented yet, using same system as player")
        self._player_action(char)

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
        if ActionPhase.is_squad_all_dead(self.squad1):
            return self.squad2.ownership
        elif ActionPhase.is_squad_all_dead(self.squad2):
            return self.squad1.ownership
        return Ownership.NULL

    @staticmethod
    def is_squad_all_dead(squad: Squad) -> bool:  # used in is_there_a_winner()
        is_squad_all_dead = True
        for char in squad.list_of_char:
            if not (char.is_dead()):
                is_squad_all_dead = False
        return is_squad_all_dead
