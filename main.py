import random

from Player import Player

#Created by bonscji1

#Globals
n_of_players = 100
num_of_round = 10

#input payoff matrix
payoffs = [[1, 3],
            [2, 4]]

probability_of_revision = 0.5

players = []

def init():
    # create number of players
    for i in range(n_of_players):
        players.append(Player(0, random.randint(0, 1)))

def play():
    print("NO")

if __name__ == '__main__':
    init()
    play()


