from battle_abilities.ability import Range, Ability
from battle_abilities.physical_atk import PhysicalAtk
from battle_abilities.spells import Spell, DmgSpell, HealingSpell
from battle_entities.char_and_squad import Character, Squad


class Action:

    def __init__(self, caster_char: Character, char_target: Character, atk_or_spell: Ability):

        self.ability = atk_or_spell

        # the amount of points an action has dealt, dmg, cure etc
        self.dmg_dealt = 0
        self.healing_dealt = 0
        self.armor_bonus_dealt = 0  # just an example

        # PHYSICAL
        if isinstance(self.ability, PhysicalAtk):
            self._physical_atk(caster_char, char_target)

        # SPELL
        elif isinstance(self.ability, Spell):
            self._launch_single_spell(caster_char, char_target, self.ability)

    def _physical_atk(self, charAtk: Character, charDef: Character) -> None:
        dmg = charAtk.weapon_dmg - charDef.armor
        self.dmg_dealt = Action._deal_dmg(charDef, dmg)

    def _launch_single_spell(self, charCaster: Character, charTarget: Character, spell: Spell) -> None:
        if charCaster.mana < spell.mana_cost:
            raise Exception(f"{spell.name} cost({spell.mana_cost}) > {charCaster.name} mana {charCaster.mana}")
        elif isinstance(spell, DmgSpell):
            self.dmg_dealt = Action._deal_dmg(charTarget, spell.effect_points)
        elif isinstance(spell, HealingSpell):
            charTarget.health += spell.effect_points
            self.healing_dealt = spell.effect_points
        charCaster.mana -= spell.mana_cost

    @staticmethod
    def _deal_dmg(char: Character, dmg: int) -> int:
        if dmg < 0:
            dmg = 0
        char.health -= dmg
        return dmg
