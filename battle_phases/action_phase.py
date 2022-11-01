import ui.battle_stats
from battle_entities.char_and_squad import Character, Ownership
from battle_phases.initiative_phase import InitiativePhase


class ActionPhase:
    def __init__(self, initiative_phase: InitiativePhase):
        self.initiative_phase = initiative_phase
        self.squad1 = self.initiative_phase.squad1
        self.squad2 = self.initiative_phase.squad2
        self.action_order_list: list[Character] = self.initiative_phase.action_order_list
        self._run_action_turn()

    def _run_action_turn(self):
        for char in self.action_order_list:
            if char.ownership == Ownership.PLAYER:
                self._player_action(char)
            elif char.ownership == Ownership.ENEMY:
                self._ai_action()
            print()  # jumps a line

    def _player_action(self, current_char: Character):

        # prints the current char
        print(f"TURN: {current_char.name}")
        print(ui.battle_stats.get_char_card(current_char))

        # picks an alive char only
        other_char: Character = None
        while other_char is None:
            chosen_char_name = input(f"Which char should {current_char.name} pick?: ").capitalize()
            for char in self.action_order_list:
                if char.name.capitalize() == chosen_char_name:
                    other_char = char
            if other_char is current_char:
                print("invalid, nao pode inflingir dano a si mesmo")
                other_char = None
            elif other_char is None:
                print("invalid char, dead or not in battle")

        # makes the atk and remove the char if its dead
        dmg = ActionPhase._physical_atk(current_char, other_char)
        self._remove_dead_chars_from_action_order_list()

        # prints battle current state
        print(f"{current_char.name} attacked {other_char.name}: tot dmg = {dmg}")
        print()
        print(ui.battle_stats.get_battle_current_state(self.initiative_phase), end="")


    @staticmethod
    def _physical_atk(charAtk: Character, charDef: Character):
        dmg: int = charAtk.weapon_dmg - charDef.armor
        if dmg < 0:
            dmg = 0
        charDef.health -= dmg
        return dmg

    def _remove_dead_chars_from_action_order_list(self):
        for char in self.action_order_list:
            if char.is_dead():
                self.action_order_list.remove(char)

    def _ai_action(self):
        print("ai action")
