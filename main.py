import random

from Player import Player
from Strategy import *

# Created by bonscji1

# Globals
n_of_players = 100
num_of_round = 10

mutation_chance = 0.05

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
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            p1 = players[i]
            p2 = players[j]
            payoffs_for_p1 = determine_payoff(p1.strategy.return_move(), p2.strategy.return_move())
            p1.score += payoffs_for_p1
            p2.score += (-1 * payoffs_for_p1)


def create_new_generation():
    highest_score_player = max(players, key=lambda player: player.score)
    for player in players:
        if random.random() < mutation_chance:
            player.strategy = highest_score_player.strategy
    return players


if __name__ == '__main__':
    init()
    for current_round in range(num_of_round):
        play_round()
        players = create_new_generation()
