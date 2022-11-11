import os
from ui import ui_resources, title_screen
from battle_abilities.spells import DmgSpell, HealingSpell
from battle_abilities.ability import Range
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.round_and_battle_management import Battle

#title_screen.execute()

ui_resources.clear_terminal()
print()
print("RULES:\n - YOU CAN ATTACK CHARS IN YOU SQUAD IT'S OKAY! \n - A CHAR CAN'T ATK ITSELF")
print()
input("press any key to continue")
ui_resources.clear_terminal()
print()

dmg_spell = DmgSpell("dano brabo", "da dano", 5, mana_cost=3, range_type=Range.SINGLE)
h_spell = HealingSpell("curar", "cura 3 de hp", 3, mana_cost=3, range_type=Range.SINGLE)

joao = Character("joao", 10, 10, 5, 20, 215, [dmg_spell, h_spell])
dani = Character("Dani", 10, 15, 2, 20, 10, [h_spell])

squad1 = Squad(Ownership.PLAYER, "player squad", [joao, dani])
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Monstrinho", 1, 2, 2, 100, 10),
                                                Character("Lobao", 3, 2, 3, 100, 10),
                                                Character("Morcego", 1, 2, 2, 100, 10)])

battle = Battle(squad1, squad2)
