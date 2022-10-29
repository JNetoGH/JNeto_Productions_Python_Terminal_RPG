from char_and_squad.battle_entities import Squad
# criar uma calsse q receba 2 squads
# checar a iniciativa de cada personagem + d20
# gerar uma lista de ordem de acao

class InitiativePhase:
    def __init__(self, squad1: Squad, squad2: Squad):
        self.squad1 = squad1
        self.squad2 = squad2