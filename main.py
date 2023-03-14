import random

from Player import Player
from Strategy import *

# Created by bonscji1

# Globals
n_of_players = 100
num_of_round = 10

# input payoff matrix
payoffs = [[1, 3],
           [2, 4]]

probability_of_revision = 0.5

players = []

rules = {
    Action.Rock: [Action.Scissors],  # Rock beats scissors
    Action.Paper: [Action.Rock],  # Paper beats rock
    Action.Scissors: [Action.Paper]  # Scissors beats paper
}

strategies = [Action.Rock, Action.Paper, Action.Scissors]


def init():
    # create number of players
    for i in range(n_of_players):
        # choose random strategies for players
        players.append(Player(0, Strategy(random.randint(0, len(Strategy)-1))))


def determine_payoff(player1_action, player2_action):
    defeats = rules[player1_action]
    if player1_action == player2_action:
        return 0
    elif player2_action in defeats:
        return 1
    else:
        return -1


def play_round():
    print("NO")

    # do i want player to play with all other players? probably
    p1 = players[0]
    p2 = players[1]
    payoffs_for_p1 = determine_payoff(p1.strategy.return_move(), p2.strategy.return_move())
    p1.score += payoffs_for_p1
    p2.score += (-1 * payoffs_for_p1)


if __name__ == '__main__':
    init()
    for current_round in range(num_of_round):
        play_round()
