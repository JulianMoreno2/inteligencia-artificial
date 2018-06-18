import numpy as np


def return_result(result):
    if result == 0:
        return (0, -1, "up")
    elif result == 1:
        return (0, 1, "down")
    elif result == 2:
        return (-1, 0, "left")
    elif result == 3:
        return (1, 0, "right")


class ActionChooser:

    def __init__(self):
        self.actions = [0, 1, 2, 3]

    def execute(self, action):
        if action == 0:
            return self.try_move_up()
        elif action == 1:
            return self.try_move_down()
        elif action == 2:
            return self.try_move_left()
        elif action == 3:
            return self.try_move_right()

    def try_move_up(self):
        result = np.random.choice(self.actions, p=[0.8, 0, 0.1, 0.1])
        return return_result(result)

    def try_move_down(self):
        result = np.random.choice(self.actions, p=[0, 0.8, 0.1, 0.1])
        return return_result(result)

    def try_move_left(self):
        result = np.random.choice(self.actions, p=[0.1, 0.1, 0.8, 0])
        return return_result(result)

    def try_move_right(self):
        result = np.random.choice(self.actions, p=[0.1, 0.1, 0, 0.8])
        return return_result(result)
