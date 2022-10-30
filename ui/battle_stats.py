# IMPORTS
from char_and_squad.battle_entities import Character

# VARS
general_length = 24

# main function
def inspect_stats(character: Character):
    print("\n" + "=" * general_length)
    print(get_centralized_stat_line(general_length, character.name))
    print("=" * general_length)
    print(get_centralized_stat_line(general_length, f"HP: {character.health}"))
    print(get_centralized_stat_line(general_length, f"Attack: {character.weapon_dmg}"))
    print(get_centralized_stat_line(general_length, f"Mana: {character.mana}"))
    print(get_centralized_stat_line(general_length, f"Armor: {character.armor}"))
    print(get_centralized_stat_line(general_length, f"Initiative: {character.initiative}"))
    print("=" * general_length)


def get_centralized_stat_line(line_length: int, msg: str) -> str:
    is_msg_length_even = len(msg) % 2 == 0
    if is_msg_length_even:
        return "|" + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + "|"
    # Adds an extra space "|" -> " |", e.g. len(msg) = 11, the division per 2 would be 5, not 5.5,
    # therefore, it would be, (line_length - 5) + msg + (line_length - 5), being discounted 10 for the msg instead o 11
    else:
        return "|" + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + " |"


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