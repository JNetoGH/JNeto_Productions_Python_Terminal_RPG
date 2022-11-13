from typing import Union
from battle_abilities.ability import Range, Ability
from battle_abilities.physical_atk import PhysicalAtk
from battle_abilities.spells import Spell, DmgSpell, HealingSpell
from battle_entities.char_and_squad import Character, Squad

# can make an Action upon a Character or a whole squad
class Action:

    def __init__(self, caster_char: Character, target: Union[Character, Squad], atk_or_spell: Ability):

        self.ability = atk_or_spell

        # the amount of points an action has dealt, dmg, cure etc
        self.dmg_dealt = 0
        self.healing_dealt = 0
        self.armor_bonus_dealt = 0  # just an example

        if isinstance(target, Character):
            # PHYSICAL
            if isinstance(self.ability, PhysicalAtk):
                self._physical_atk(caster_char, target)
            # SPELL
            elif isinstance(self.ability, Spell):
                self._decrease_mana_for_spell(caster_char, self.ability)
                self._launch_single_spell(target, self.ability)
        elif isinstance(target, Squad):
            # PHYSICAL
            """
            if isinstance(self.ability, PhysicalAtk):
                targets: list[Character] = target.list_of_char
                for char in targets:
                    self._physical_atk(caster_char, char)
            """
            # SPELL
            if isinstance(self.ability, Spell):
                self._decrease_mana_for_spell(caster_char, self.ability)
                for char in target.list_of_char:
                    self._launch_single_spell(char, self.ability)

    def _physical_atk(self, charAtk: Character, charDef: Character) -> None:
        dmg = charAtk.weapon_dmg - charDef.armor
        self.dmg_dealt = Action._deal_dmg(charDef, dmg)

    def _launch_single_spell(self, charTarget: Character, spell: Spell) -> None:
        if isinstance(spell, DmgSpell):
            self.dmg_dealt = Action._deal_dmg(charTarget, spell.effect_points)
        elif isinstance(spell, HealingSpell):
            if not charTarget.is_dead():
                charTarget.health += spell.effect_points
                self.healing_dealt = spell.effect_points

    def _decrease_mana_for_spell(self, charCaster: Character, spell: Spell):
        if charCaster.mana < spell.mana_cost:
            raise Exception(f"{spell.name} cost({spell.mana_cost}) > {charCaster.name} mana {charCaster.mana}")
        charCaster.mana -= spell.mana_cost

    @staticmethod
    def _deal_dmg(char: Character, dmg: int) -> int:
        if dmg < 0:
            dmg = 0
        char.health -= dmg
        if char.health < 0:
            char.health = 0
        return dmg
