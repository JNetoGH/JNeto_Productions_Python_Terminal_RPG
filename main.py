from ui import ui_resources, title_screen
from battle_abilities.ability import *
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.round_and_battle_management import Battle

#title_screen.execute()

ui_resources.clear_terminal()
input("press enter to start\n")
ui_resources.clear_terminal()
print()

dmg_spell = DmgSpell("dano brabo", "da dano", 210, mana_cost=2)
h_spell = HealingSpell("curar", "cura 3 de hp", 3, mana_cost=3, can_affect_allies=True, can_affect_caster=True)


joao = Character("joao", 10, 10, 5, 20, 215, [dmg_spell])
dani = Character("Dani", 10, 15, 2, 20, 10, [h_spell])

squad1 = Squad(Ownership.PLAYER, "player squad", [joao, dani])
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Monstrinho", 2, 2, 2, 100, 10),
                                                Character("Lobao", 2, 2, 3, 100, 10),
                                                Character("Morcego", 2, 2, 2, 100, 10)])

battle = Battle(squad1, squad2)
