# NAO PODE SER IMPAR
GENERAL_LINE_LENGTH = 24

# DOUBLE LINES
GENERAL_WALL = "║"
GENERAL_LINE = "═"
GENERAL_UP_LEFT_CORNER = "╔"
GENERAL_BOTTOM_LEFT_CORNER = "╚"
GENERAL_UP_RIGHT_CORNER = "╗"
GENERAL_BOTTOM_RIGHT_CORNER = "╝"

# LIGHT SINGLE LINES
GENERAL_LIGHT_LINE = "─"
GENERAL_LIGHT_LEFT_CONNECTOR = "╟"
GENERAL_LIGHT_RIGHT_CONNECTOR = "╢"


def get_char_card(char, line_length: int = GENERAL_LINE_LENGTH) -> str:
    card = f"{GENERAL_UP_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_UP_RIGHT_CORNER}\n"
    card += get_centralized_stat_line(line_length, char.name, GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}\n"
    card += get_centralized_stat_line(line_length, f"HP: {char.health}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Attack: {char.weapon_dmg}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Mana: {char.mana}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Armor: {char.armor}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_stat_line(line_length, f"Initiative: {char.initiative}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_BOTTOM_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_BOTTOM_RIGHT_CORNER}"
    return card


def get_squad_char_cards_inline(squad, line_length: int = GENERAL_LINE_LENGTH) -> str:
    padding = 3
    squad_char_cards_inline = ""
    for i in range(0, 9):
        add_line_break = i != 8
        squad_char_cards_inline += _get_char_card_squad_line(squad, i, line_length, padding, add_line_break)
    return squad_char_cards_inline


# concatenates the all the chars cards (x line) into one single line, separated with a padding
def _get_char_card_squad_line(squad, line_index, line_length, padding, add_line_break: bool) -> str:
    line = ""
    for char in squad.list_of_char:

        # used to print the card as red
        code1 = ""
        code2 = "\033[0m"
        if char.is_dead():
            code1 = "\033[91m"
        line += code1

        if line_index == 0:
            line += f"{GENERAL_UP_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_UP_RIGHT_CORNER}" + " " * padding
        elif line_index == 1:
            line += get_centralized_stat_line(line_length, char.name, GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 2:
            line += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}" + " " * padding
        elif line_index == 3:
            line += get_centralized_stat_line(line_length, f"HP: {char.health}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 4:
            line += get_centralized_stat_line(line_length, f"Attack: {char.weapon_dmg}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 5:
            line += get_centralized_stat_line(line_length, f"Mana: {char.mana}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 6:
            line += get_centralized_stat_line(line_length, f"Armor: {char.armor}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 7:
            line += get_centralized_stat_line(line_length, f"Initiative: {char.initiative}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 8:
            line += f"{GENERAL_BOTTOM_LEFT_CORNER}{GENERAL_LINE * (line_length - 2)}{GENERAL_BOTTOM_RIGHT_CORNER}" + " " * padding

        # used to print the card as red
        line += code2

    if add_line_break:
        line += "\n"
    return line


def get_centralized_stat_line(line_length: int, msg: str = "Default", wall1: str = " ", wall2: str = " ") -> str:
    if line_length % 2 != 0:
        raise Exception("lines can't be set with an odd length, only even")

    is_msg_length_even = len(msg) % 2 == 0
    if is_msg_length_even:
        return wall1 + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (
                    int((line_length / 2 - len(msg) / 2)) - 1) + wall2
    # Adds an extra space "|" -> " |", e.g. len(msg) = 11, the division per 2 would be 5, not 5.5,
    # therefore, it would be, (line_length - 5) + msg + (line_length - 5), being discounted 10 for the msg instead o 11
    else:
        return wall1 + " " * (int((line_length / 2 - len(msg) / 2)) - 1) + msg + " " * (
                    int((line_length / 2 - len(msg) / 2)) - 1) + " " + wall2
