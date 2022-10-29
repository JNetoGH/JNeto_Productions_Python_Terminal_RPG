from char_and_squad.battle_entities import Character, Squad
from battle_phases.initiative_phase import InitiativePhase

squad1 = Squad("player squad", [Character("Joao", 10, 5, 5, 5, 10), Character("Dani", 10, 5, 5, 5, 10), Character("Lulu", 0, 5, 5, 5, 10)])
squad2 = Squad("enemy squad", [Character("Monstrinho", 10, 5, 5, 5, 10), Character("Lobao", 10, 5, 5, 5, 10), Character("Morcego", 0, 5, 5, 5, 10)])
initiative_phase = InitiativePhase(squad1, squad2)

print(squad1.to_string())
print()
print(squad2.to_string())
print()
print(initiative_phase.to_string())

for char in initiative_phase.action_order_list:
    print(char)
