# IMPORTS
from char_and_squad.battle_entities import Character

# NAO PODE SER IMPAR
GENERAL_LINE_LENGTH = 24

# DOUBLE LINES
GENERAL_WALL = "║"
GENERAL_LINE = "═"
GENERAL_UP_LEFT_CORNER = "╔"
GENERAL_BOTTOM_LEFT_CORNER = "╚"
GENERAL_UP_RIGHT_CORNER = "╗"
GENERAL_BOTTOM_RIGHT_CORNER = "╝"

# LIGHT SINGLE LINES
GENERAL_LIGHT_LINE = "─"
GENERAL_LIGHT_LEFT_CONNECTOR = "╟"
GENERAL_LIGHT_RIGHT_CONNECTOR = "╢"


def get_char_card(character: Character, line_length: int):
    card = f"{GENERAL_UP_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_UP_RIGHT_CORNER}\n"
    card += get_centralized_stat_line(line_length, character.name, GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}\n"
    card += get_centralized_stat_line(line_length, f"HP: {character.health}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Attack: {character.weapon_dmg}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Mana: {character.mana}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Armor: {character.armor}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Initiative: {character.initiative}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_BOTTOM_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_BOTTOM_RIGHT_CORNER}\n"
    return card


def get_centralized_stat_line(line_length: int, msg: str = "Default", wall1: str = " ", wall2: str = " ") -> str:
    is_msg_length_even = len(msg) % 2 == 0
    if is_msg_length_even:
        return wall1 + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + wall2
    # Adds an extra space "|" -> " |", e.g. len(msg) = 11, the division per 2 would be 5, not 5.5,
    # therefore, it would be, (line_length - 5) + msg + (line_length - 5), being discounted 10 for the msg instead o 11
    else:
        return wall1 + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + " " + wall2



"""
# playable branch
while True:
    print(f"\nOPTIONS: \n[1]   Fight\n[2]   Flee\n[3]   Inspect Enemy")
    choice = int(input())
    if choice == 1:
        print("\n\n FIGHTING IN PROGRESS...")
    elif choice == 3:
        print("\n Choose enemy to inspect.\n[1]   Monstrinho")
        ins = int(input())
        if ins == 1:
            inspectStats("Monstrinho")
    elif choice == 2:
        succ: int = random.randrange(1, 10)
        print(succ)
        if succ >= 5:
            print("\n You flee!")
        else:
            print("\nFAILED FLEEING. \n STARTING FIGHTING...\n\nYou lose your initiative for this round.")
"""