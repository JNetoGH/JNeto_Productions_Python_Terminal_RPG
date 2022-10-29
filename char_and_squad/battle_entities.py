class Character:

    def __init__(self, name: str, health: int, mana: int, armor: int, weapon_dmg: int, initiative: int):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative
        self.turnOrder = 0

    def is_dead(self) -> bool:
        return self.health <= 0

    def to_string(self) -> str:
        txt: str = f"{self.name} \nINITIATIVE: {self.initiative} | HP: {self.health} | MANA: {self.mana} " \
                   f"| ARMOR: {self.armor} | W_DMG: {self.weapon_dmg} | is dead: {self.is_dead()}"
        # adds the color red when a character is dead
        if self.is_dead():
            txt = "\033[91m" + txt + "\033[0m"
        return txt


class Squad:

    def __init__(self, squad_name: str, list_of_char: list[Character]):
        self.squad_name = squad_name
        self.list_of_char = list_of_char

    def to_string(self) -> str:
        line_length: int = 75
        text: str = "="*line_length + "\n" + f"Squad ({self.squad_name}) \n" + "-"*line_length + "\n"
        for i in range(0, len(self.list_of_char)):
            text += self.list_of_char[i].to_string()
            if i != len(self.list_of_char) - 1:
                text += "\n" + "-"*line_length + "\n"
            else:
                text += "\n"
        text += "="*line_length
        return text
