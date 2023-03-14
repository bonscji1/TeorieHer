import random

from Player import Player
from Strategy import *

# Created by bonscji1

# Globals

# number of players needs to be > 1
n_of_players = 100

# number of round, needs to be > 0
num_of_round = 10

#
# needs to be between 0 and 1
survival_percentage = 0.95

#
# needs to be between 0 and 1
mutation_chance = 0.05

# game rules
rules = {
    Action.Rock: [Action.Scissors],  # Rock beats scissors
    Action.Paper: [Action.Rock],  # Paper beats rock
    Action.Scissors: [Action.Paper]  # Scissors beats paper
}
# game strategies
strategies = [Action.Rock, Action.Paper, Action.Scissors]

players = []

def init():
    # blbuvzdornost
    if num_of_round < 1:
        raise ValueError("num_of_round is not valid")
    elif n_of_players < 2:
        raise ValueError("n_of_players is not valid")
    elif survival_percentage < 0 or survival_percentage > 1:
        raise ValueError("survival_percentage is not valid")
    elif mutation_chance < 0 or mutation_chance > 1:
        raise ValueError("mutation_chance is not valid")

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
    #todo
    # return score to zero for survivors
    # kill lower half, create new ones, from the ones we got and mutate som of the new ones
    highest_score_player = max(players, key=lambda player: player.score)
    for player in players:
        if random.random() < mutation_chance:
            player.strategy = highest_score_player.strategy
    return players

def print_round_stats():
    total_score = sum(player.score for player in players)
    mean_score = total_score / len(players)
    worst_player = min(players, key=lambda player: player.score)
    best_player = max(players, key=lambda player: player.score)
    print(f"round: {current_round+1} \n"
          f"mean score of players: {mean_score}\n"
          f"worst player in this round achieved score: {worst_player.score} with strategy: {worst_player.strategy.output()}\n"
          f"best player in this round achieved score: {best_player.score} with strategy: {best_player.strategy.output()}")

if __name__ == '__main__':
    init()
    for current_round in range(num_of_round):
        play_round()
        print_round_stats()
        players = create_new_generation()




