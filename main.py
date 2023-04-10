import random
from bke import start, MLAgent, EvaluationAgent, is_winner, opponent, train_and_plot, can_win, train, save, load 

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 10
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

