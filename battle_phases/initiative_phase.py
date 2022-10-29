from char_and_squad.battle_entities import Squad, Character
from random import *
import enum


class CharCodes(enum.Enum):
    DeadChar = -1


class InitiativePhase:

    def __init__(self, squad1: Squad, squad2: Squad):
        self.action_order_list: list[Character] = []  # this class just exists in order to generate this list
        self._generate_turn_orders_of_a_squad(squad1)
        self._generate_turn_orders_of_a_squad(squad2)
        self._treat_and_add_squad_to_action_order_list(squad1)
        self._treat_and_add_squad_to_action_order_list(squad2)
        self._insertion_sort_action_order_list()

    @staticmethod
    def _d20() -> int:
        result = randrange(1, 20)
        return result

    @staticmethod
    def _generate_turn_orders_of_a_squad(squad: Squad) -> None:
        for char in squad.list_of_char:
            if char.is_dead():
                char.turnOrder = CharCodes.DeadChar
            else:
                char.turnOrder = char.initiative + InitiativePhase._d20()

    def _treat_and_add_squad_to_action_order_list(self, squad_to_be_added: Squad) -> None:
        for char in squad_to_be_added.list_of_char:
            if char.turnOrder != CharCodes.DeadChar:  # simply adds the chars to the list, except the dead ones
                self.action_order_list.append(char)

    def _insertion_sort_action_order_list(self) -> None:
        for i in range(1, len(self.action_order_list)):  # iterate over unsorted array
            val = self.action_order_list[i]  # get element value
            hole = i  # insertion "hole" is at index i
            # loop backwards until a value greater than current value is found
            while hole > 0 and self.action_order_list[hole - 1].turnOrder < val.turnOrder:
                self.action_order_list[hole] = self.action_order_list[hole - 1]  # swap elements towards correct pos
                hole -= 1  # move backwards
            self.action_order_list[hole] = val  # insert value into correct position

    def to_string(self) -> str:
        text = "ACTION ORDER: \n| "
        for char in self.action_order_list:
            text += f"{char.name}: {char.turnOrder}(init+D20:{char.turnOrder - char.initiative}) | "
        return text
