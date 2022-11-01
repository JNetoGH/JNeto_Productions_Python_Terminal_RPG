from battle_entities.char_and_squad import Squad, Ownership
from battle_phases.initiative_phase import InitiativePhase
from battle_phases.action_phase import ActionPhase


class Round:
    def __init__(self, initiativePhase: InitiativePhase):
        self.initiativePhase = initiativePhase
        self.actionPhase = ActionPhase(initiativePhase)


class Battle:
    def __init__(self, squad1: Squad, squad2: Squad):

        current_round = None

        while True:

            current_round = Round(InitiativePhase(squad1, squad2))

            if current_round.actionPhase.force_quit_battle:
                print("exit battle")
                break

            if current_round.actionPhase.is_there_a_winner() != Ownership.NULL:
                if current_round.actionPhase.is_there_a_winner() == Ownership.PLAYER:
                    print("player venceu")
                elif current_round.actionPhase.is_there_a_winner() == Ownership.ENEMY:
                    print("enemy venceu")
                break
            else:
                print("action_order_list is empty")
                print("another round will be generated")
                input("press any key to generate another round")

        print("Battle finished")




