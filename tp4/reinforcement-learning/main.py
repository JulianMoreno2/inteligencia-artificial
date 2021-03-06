from board import Board
from learner import QLearner
from action_chooser import ActionChooser
import threading

alpha = 0.8
size = 5
walk_reward = -0.1
lose_reward = -10
win_reward = 10
board = Board(size, walk_reward, lose_reward, win_reward)
q_learner = QLearner(board, ActionChooser(), alpha)

t = threading.Thread(target=q_learner.run)

t.daemon = True
t.start()
board.start_game()
