
from enum import IntEnum


class Strategy(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

    def return_move(self):
        if self == Strategy.Rock:
            return Action.Rock
        elif self == Strategy.Paper:
            return Action.Paper
        elif self == Strategy.Scissors:
            return Action.Scissors

    def output(self):
        if self == Strategy.Rock:
            return "Rock"
        elif self == Strategy.Paper:
            return "Paper"
        elif self == Strategy.Scissors:
            return "Scissors"

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

