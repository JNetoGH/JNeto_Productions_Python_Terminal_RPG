import ui.battle_stats
from battle_entities.char_and_squad import Character, Ownership
from battle_phases.initiative_phase import InitiativePhase


class ActionPhase:
    def __init__(self, initiative_phase: InitiativePhase):
        self.initiative_phase = initiative_phase
        self.squad1 = self.initiative_phase.squad1
        self.squad2 = self.initiative_phase.squad2
        self.action_order_list: list[Character] = self.initiative_phase.action_order_list
        self.all_chars = self.action_order_list.copy()

        counter = 0
        while self.is_there_a_winner() == Ownership.NULL or len(self.action_order_list) != 0:
            if len(self.action_order_list) != 0:
                current_char = self.action_order_list[0]
                self._run_action_turn(current_char)
                self.remove_a_char_from_action_order_list(current_char)
                self.remove_dead_chars_from_action_order_list()
                print(ui.battle_stats.get_battle_current_state(self.initiative_phase), end="")

        if self.is_there_a_winner() == Ownership.PLAYER:
            print("player venceu")
        elif self.is_there_a_winner() == Ownership.ENEMY:
            print("enemy venceu")
        elif self.is_there_a_winner() == Ownership.NULL:
            print("algo de estranhoa conteceu")

    def is_there_a_winner(self) -> Ownership:
        is_squad1_all_dead = True
        for char in self.squad1.list_of_char:
            if not(char.is_dead()):
                is_squad1_all_dead = False
        if is_squad1_all_dead:
            return self.squad1.ownership
        is_squad2_all_dead = True
        for char in self.squad2.list_of_char:
            if not(char.is_dead()):
                is_squad2_all_dead = False
        if is_squad2_all_dead:
            return self.squad2.ownership
        return Ownership.NULL

    def remove_dead_chars_from_action_order_list(self) -> bool:
        for char in self.action_order_list:
            if char.is_dead():
                self.action_order_list.remove(char)
                return True

    def remove_a_char_from_action_order_list(self, char: Character) -> bool:
        if char in self.action_order_list:
            self.action_order_list.remove(char)
            return True

    def _run_action_turn(self, char: Character):
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
            for char in self.all_chars:
                if char.name.capitalize() == chosen_char_name:
                    other_char = char
            if other_char is current_char:
                print("invalid, nao pode inflingir dano a si mesmo")
                other_char = None
            elif other_char.is_dead():
                print(f"invalid, {other_char} is already dead")
                other_char = None
            elif other_char is None:
                print("invalid char does not exist")

        # makes the atk and remove the char if its dead
        dmg = ActionPhase._physical_atk(current_char, other_char)

        # prints battle current state
        print(f"{current_char.name} attacked {other_char.name}: tot dmg = {dmg}")
        print()


    @staticmethod
    def _physical_atk(charAtk: Character, charDef: Character):
        dmg: int = charAtk.weapon_dmg - charDef.armor
        if dmg < 0:
            dmg = 0
        charDef.health -= dmg
        return dmg


    def _ai_action(self):
        print("ai action")


