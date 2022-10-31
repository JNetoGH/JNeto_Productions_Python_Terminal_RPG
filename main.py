import ui.battle_stats
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_phases.initiative_phase import InitiativePhase

squad1 = Squad(Ownership.PLAYER, "player squad", [Character("Joao", 10, 5, 5, 5, 10), Character("Dani", 10, 5, 5, 5, 10), Character("Lulu", 0, 5, 5, 5, 10)])
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Monstrinho", 0, 85, 115, 5, 10), Character("Lobao", 10, 5, 5, 5, 10), Character("Morcego", 0, 5, 5, 5, 10)])
initiative_phase = InitiativePhase(squad1, squad2)


print("="*80)
print(squad1.to_string())
print("-"*38 + "VS" +  "-"*38)
print(squad2.to_string())
print("="*80)
print()
print(initiative_phase.to_string())
print()
print("="*80)
"""
print(squad1.list_of_char[0].to_string())
print(squad2.to_string())
"""