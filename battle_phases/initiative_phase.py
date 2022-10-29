from char_and_squad.battle_entities import Squad, Character
from random import *
import enum


class CharCodes(enum.Enum):
    DeadChar = -1


class InitiativePhase:

    def __init__(self, squad1: Squad, squad2: Squad):
        self.squad1 = squad1
        self.squad2 = squad2
        self.generate_turn_orders(self.squad1)
        self.generate_turn_orders(self.squad2)
        self.action_order_list: list[Character] = []
        self.init_action_order_list()
        self.insertion_sort_action_order_list()

    def d20(self):
        result = randrange(1, 20)
        return result

    def generate_turn_orders(self, squad: Squad):
        for char in squad.list_of_char:
            if char.is_dead():
                char.turnOrder = CharCodes.DeadChar
            else:
                char.turnOrder = char.initiative + self.d20()

    def init_action_order_list(self):
        for char in self.squad1.list_of_char:
            if char.turnOrder != CharCodes.DeadChar:
                self.action_order_list.append(char)
        for char in self.squad2.list_of_char:
            if char.turnOrder != CharCodes.DeadChar:
                self.action_order_list.append(char)

    def insertion_sort_action_order_list(self):
        # iterate over unsorted array
        for i in range(1, len(self.action_order_list)):
            # get element value
            val = self.action_order_list[i]
            # insertion "hole" is at index i
            hole = i
            # loop backwards until a value greater than current value is found
            while hole > 0 and self.action_order_list[hole - 1].turnOrder < val.turnOrder:
                # swap elements towards correct position
                self.action_order_list[hole] = self.action_order_list[hole - 1]
                # move backwards
                hole -= 1
            # insert value into correct position
            self.action_order_list[hole] = val

    def to_string(self):
        text = "ACTION ORDER: | "
        for i in range(0, len(self.action_order_list)):
            text += f"{self.action_order_list[i].name}: {self.action_order_list[i].turnOrder} | "
        return text
