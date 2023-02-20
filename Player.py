class Player:
    # player class, should contain what player has and can do
    def __init__(self, payoff, strategy):
        self.payoff = payoff
        self.strategy = strategy  #should be either 0 or 1 for now
