from ui import ui_resources
from battle_abilities.ability import *
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.round_and_battle_management import Battle

ui_resources.clear_terminal()
input("press enter to start\n")
ui_resources.clear_terminal()
print()

dmg_spell = DmgSpell("dano brabo", "da 10 de dano", 10, mana_cost=2)
daninho_spell = DmgSpell("daninho", "da 5 de dano", 5, mana_cost=1)
stor_spell_Rush_Down = RushDown()
stor_spell_Exorcism = Exorcism()
h_spell = HealingSpell("curar", "cura 3 de hp", 3, mana_cost=3, can_affect_allies=True, can_affect_caster=True)

joao = Character("Warrior", 32, 5, 2, 5, 2, [dmg_spell, daninho_spell, stor_spell_Rush_Down])
dani = Character("Priest", 20, 25, 0, 2, 6, [stor_spell_Exorcism, h_spell])
squad1 = Squad(Ownership.PLAYER, "player squad", [joao, dani])

squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Speedy", 2, 0, 1, 1, 10),
                                                Character("Orc", 15, 0, 2, 2, 2),
                                                Character("Speedy", 2, 0, 1, 1, 10)])

battle = Battle(squad1, squad2)
