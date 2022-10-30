from char_and_squad.battle_entities import Character, Squad
from battle_phases.initiative_phase import InitiativePhase
from ui.battle_stats import GENERAL_LINE_LENGTH, get_char_card, get_squad_char_cards_inline

squad1 = Squad("player squad", [Character("Joao", 10, 5, 5, 5, 10), Character("Dani", 10, 5, 5, 5, 10), Character("Lulu", 0, 5, 5, 5, 10)])
squad2 = Squad("enemy squad", [Character("Monstrinho", 0, 85, 115, 5, 10), Character("Lobao", 10, 5, 5, 5, 10), Character("Morcego", 0, 5, 5, 5, 10)])
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