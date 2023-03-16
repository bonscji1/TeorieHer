import math
import random

from Player import Player
from Strategy import *

# Created by bonscji1

# Globals

# number of players needs to be > 1
n_of_players = 1000

# number of round, needs to be > 0
num_of_round = 20

#
# needs to be between 0 and 1
percentage_to_remove = 0.05

#
# needs to be between 0 and 1
mutation_chance = 0.05

# game rules
rules = {
    Action.Rock: [Action.Scissors],  # Rock beats scissors
    Action.Paper: [Action.Rock],  # Paper beats rock
    Action.Scissors: [Action.Paper]  # Scissors beats paper
}

players = []


def init():
    # blbuvzdornost
    if num_of_round < 1:
        raise ValueError("num_of_round is not valid")
    elif n_of_players < 2:
        raise ValueError("n_of_players is not valid")
    elif percentage_to_remove < 0 or percentage_to_remove > 1:
        raise ValueError("survival_percentage is not valid")
    elif mutation_chance < 0 or mutation_chance > 1:
        raise ValueError("mutation_chance is not valid")

    # create number of players
    for i in range(n_of_players):
        # choose random strategies for players
        players.append(Player(0, getRandomStrategy()))


def getRandomStrategy():
    return Strategy(random.randint(0, len(Strategy) - 1))


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
        for j in range(i + 1, len(players)):
            p1 = players[i]
            p2 = players[j]
            payoffs_for_p1 = determine_payoff(p1.strategy.return_move(), p2.strategy.return_move())
            p1.score += payoffs_for_p1
            p2.score += (-1 * payoffs_for_p1)


def create_new_generation(oldOnes):
    # calculate number of players to remove
    num_players_to_remove = math.ceil(len(oldOnes) * percentage_to_remove)

    # sort players
    sorted_ones = sorted(oldOnes, key=lambda player: player.score)

    # remove the players with the lowest scores
    dead = sorted_ones[:num_players_to_remove]
    survivors = sorted_ones[num_players_to_remove:]
    # reset score
    for player in survivors:
        player.score = 0

    children = []
    # replenish players by creating children randomly with mutation chance
    for i in enumerate(dead):
        if random.random() < mutation_chance:
            children.append(Player(0, getRandomStrategy()))
        else:
            children.append(survivors[random.randint(0, len(survivors) - 1)])

    return survivors + children


def print_round_stats():
    total_score = sum(player.score for player in players)
    mean_score = total_score / len(players)
    worst_player = min(players, key=lambda player: player.score)
    best_player = max(players, key=lambda player: player.score)
    print(f"round: {current_round + 1} \n"
          f"mean score of players: {mean_score}\n"
          f"worst player in this round achieved score: {worst_player.score} with strategy: {worst_player.strategy.output()}\n"
          f"best player in this round achieved score: {best_player.score} with strategy: {best_player.strategy.output()}")


if __name__ == '__main__':
    init()
    for current_round in range(num_of_round):
        play_round()
        print_round_stats()
        players = create_new_generation(players)
