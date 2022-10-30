# Exemplo

# IMPORTS
import random
from main import char

# VARS
leth = 23


# main function
def inspectStats(character):
    if character == "Monstrinho":
        print("\n" + "=" * leth)
        print("|" + " " * 5 + "Monstrinho" + " " * 6 + "|")
        print("=" * leth)
        print("|" + " " * 5 + f"HP : {char.health}" + " " * 9 + "|")
        print("|" + " " * 5 + f"Attack : {char.weapon_dmg}" + " " * 6 + "|")
        print("|" + " " * 5 + f"Mana : {char.mana}" + " " * 8 + "|")
        print("|" + " " * 5 + f"Initiative : {char.initiative}" + " " * 1 + "|")
        print("|" + " " * 5 + f"Armor : {char.armor}" + " " * 7 + "|")
        print("=" * leth)


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
