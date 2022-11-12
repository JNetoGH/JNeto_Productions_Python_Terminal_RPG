from ui import battle_stats
from typing import Union
from battle_abilities.ability import Range
from battle_abilities.physical_atk import PhysicalAtk
from battle_abilities.spells import Spell
from battle_core.action_phase_and_dependencies.action import Action
from battle_entities.char_and_squad import Character


# It manages the user's input in order to make an action.
# The Action Phase Caller is required only to set the skip and quit battle option at the Phase Loop
class PlayerActionManager:

    def __init__(self, ActionPhaseCaller, current_char: Character, all_chars):

        self.all_chars = all_chars
        print(f"\nTURN: {current_char.name}")
        print(battle_stats.get_char_card(current_char))  # prints the current char card

        action_done = False
        while not action_done:

            action_kind = input(f"What should {current_char.name} do? [1:Atk] [2:Spell] [3:Skip] [4:Quit]: ")

            if action_kind.capitalize() == "Atk" or action_kind == "1":
                target_char: Character = self._try_get_a_target_by_name_from_player(current_char, can_pick_itself=False)
                if target_char == "RETURN":
                    action_done = False
                else:
                    action = Action(current_char, target_char, PhysicalAtk(Range.SINGLE, can_affect_caster=False))
                    dmg = action.dmg_dealt
                    print(f"{current_char.name} attacked {target_char.name}: tot dmg = {dmg}\n")
                    action_done = True

            elif action_kind.capitalize() == "Spell" or action_kind == "2":
                spell = PlayerActionManager.try_get_a_valid_spell_in_char_from_player_or_return_code(current_char)
                # in case the player has chosen return spell won't be a Spell, will be -1
                if isinstance(spell, Spell):
                    target_char = self._try_get_a_target_by_name_from_player(current_char, spell.can_affect_caster)
                    if target_char == "RETURN":
                        action_done = False
                    else:
                        try:
                            action = Action(current_char, target_char, spell)
                            action_done = True
                        except:
                            print(f"{current_char.name} doesn't have enough mana ({current_char.mana}) to cast "
                                  f"{spell.name} (cost:{spell.mana_cost})")

            elif action_kind.capitalize() == "Skip" or action_kind == "3":
                ActionPhaseCaller._force_skip_turn, action_done = True, True

            elif action_kind.capitalize() == "Quit" or action_kind == "4":
                ActionPhaseCaller.force_quit_battle, action_done = True, True

    @staticmethod
    def try_get_a_valid_spell_in_char_from_player_or_return_code(current_char: Character) -> Union[Spell, str]:
        if not current_char.have_spells():
            print(f"invalid, {current_char.name} doesn't have any spells")
        else:
            battle_stats.display_char_spells(current_char)
            while True:  # gets a valid spell asking its index
                spell_input = input("insert a spell number or type return to choose another action: ")
                if spell_input.upper() == "RETURN":
                    return "RETURN"
                elif not (spell_input.isnumeric()):
                    print("invalid input, please insert a index")
                elif spell_input.isnumeric():
                    spell_index = int(spell_input)
                    if 0 <= spell_index < len(current_char.spells):
                        return current_char.spells[spell_index]
                    else:
                        print(f"invalid input, there is no spell with index {spell_input}")

    def _try_get_a_target_by_name_from_player(self, current_char: Character, can_pick_itself: bool) -> Union[Character, str]:
        target_char: Character = None
        while target_char is None:
            chosen_char_name = input(f"Which char should {current_char.name} pick? insert its name or type return: ").capitalize()
            if chosen_char_name.upper() == "RETURN":
                return "RETURN"
            for char in self.all_chars:
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
