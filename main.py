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

class RandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1 
    if can_win(board, opponent_symbol):
      getal = getal = 1000
    return getal
