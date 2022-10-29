class Character:

    def __init__(self, name, health, mana, armor, weapon_dmg, initiative):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative
        self.turnOrder = 0

    def is_dead(self):
        return self.health <= 0

    def to_string(self) -> str:
        txt: str = f"NAME: {self.name} | INITIATIVE: {self.initiative} \n" \
                   f"HP: {self.health} | MANA: {self.mana} | ARMOR: {self.armor} | W_DMG: {self.weapon_dmg}\n" \
                   f"is dead: {self.is_dead()}"
        if self.is_dead():
            txt = "\033[91m" + txt + "\033[0m"
        return txt


class Squad:

    def __init__(self, squad_name: str, list_of_char: list[Character]):
        self.squad_name = squad_name
        self.list_of_char = list_of_char

    def to_string(self):
        width = 45
        text: str = "="*width + "\n" + f"Squad: {self.squad_name} \n" + "-"*width + "\n"
        for i in range(0, len(self.list_of_char)):
            text += self.list_of_char[i].to_string()
            if i != len(self.list_of_char) - 1:
                text += "\n" + "-"*width + "\n"
            else:
                text += "\n"
        text += "="*width
        return text
