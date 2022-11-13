from ui import ui_resources, title_screen
from battle_abilities.spells import DmgSpell, HealingSpell
from battle_abilities.ability import Range
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.round_and_battle_management import Battle

#title_screen.execute()

ui_resources.clear_terminal()
print("\nRULES:\n - YOU CAN ATTACK CHARS IN YOU SQUAD IT'S OKAY! \n - A CHAR CAN'T ATK ITSELF\n")
input("press enter to continue\n")
ui_resources.clear_terminal()
print()

dmg_spell = DmgSpell("dano brabo", "da dano", 5, mana_cost=3, range_type=Range.SINGLE, can_affect_caster=False)
area_dmg_spell = DmgSpell("dano em area", "da dano em toda a squad inimiga", 4,mana_cost=3, range_type=Range.AREA, can_affect_caster=False)
h_spell = HealingSpell("curar", "cura 3 de hp", 3, mana_cost=3, range_type=Range.SINGLE, can_affect_caster=True)
h_spell_area = HealingSpell("curar em area", "cura 10 de hp da sua squad", 10, mana_cost=3, range_type=Range.AREA, can_affect_caster=True)

joao = Character("joao", 10, 10, 5, 20, 215, [dmg_spell, area_dmg_spell])
dani = Character("Dani", 10, 15, 2, 20, 10, [h_spell, h_spell_area])

squad1 = Squad(Ownership.PLAYER, "player squad", [joao, dani])
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Monstrinho", 2, 2, 2, 100, 10),
                                                Character("Lobao", 2, 2, 3, 100, 10),
                                                Character("Morcego", 2, 2, 2, 100, 10)])

battle = Battle(squad1, squad2)
