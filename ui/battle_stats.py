# IMPORTS
from char_and_squad.battle_entities import Character

# VARS
general_line_length = 24

# DOUBLE LINES
general_wall = "║"
general_line = "═"
general_up_left_corner = "╔"
general_bottom_left_corner = "╚"
general_up_right_corner = "╗"
general_bottom_right_corner = "╝"

# LIGHT SINGLE LINES
general_light_line = "─"
general_light_line_left_connector = "╟"
general_light_line_right_connector = "╢"


def inspect_stats(character: Character):
    print(f"{general_up_left_corner}{(general_line * (general_line_length - 2))}{general_up_right_corner}")
    print(get_centralized_stat_line(general_line_length, character.name, general_wall, general_wall))
    print(f"{general_light_line_left_connector}{general_light_line * (general_line_length - 2)}{general_light_line_right_connector}")
    print(get_centralized_stat_line(general_line_length, f"HP: {character.health}", general_wall, general_wall))
    print(get_centralized_stat_line(general_line_length, f"Attack: {character.weapon_dmg}", general_wall, general_wall))
    print(get_centralized_stat_line(general_line_length, f"Mana: {character.mana}", general_wall, general_wall))
    print(get_centralized_stat_line(general_line_length, f"Armor: {character.armor}", general_wall, general_wall))
    print(get_centralized_stat_line(general_line_length, f"Initiative: {character.initiative}", general_wall, general_wall))
    print(f"{general_bottom_left_corner}{(general_line * (general_line_length - 2))}{general_bottom_right_corner}")


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