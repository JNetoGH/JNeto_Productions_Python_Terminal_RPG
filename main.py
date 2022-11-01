from ui.battle_stats import *
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_phases.action_phase import ActionPhase
from battle_phases.initiative_phase import InitiativePhase

print()
print("RULES:\n - YOU CAN ATTACK CHARS IN YOU SQUAD IT'S OKAY! \n - A CHAR CAN'T ATK ITSELF")

squad1 = Squad(Ownership.PLAYER, "player squad", [Character("joao", 10, 15, 5, 20, 10), Character("Dani", 10, 15, 2, 20, 10), Character("Lulu", 1, 5, 5, 5, 10)])
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Monstrinho", 1, 85, 115, 5, 10), Character("Lobao", 10, 2, 3, 5, 10), Character("Morcego", 1, 5, 5, 5, 10)])
initiative_phase = InitiativePhase(squad1, squad2)

print()
print(get_battle_current_state(initiative_phase))
action_phase = ActionPhase(initiative_phase)

"""
print(squad1.list_of_char[0].to_string())
print(squad2.to_string())
"""