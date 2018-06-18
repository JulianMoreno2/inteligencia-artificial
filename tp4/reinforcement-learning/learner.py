import time


class QLearner:

    def __init__(self, board, action_chooser, alpha):

        self.board = board
        self.action_chooser = action_chooser
        self.alpha = alpha
        self.board.render_grid()
        self.actions = self.board.get_actions()
        self.states = []
        self.Q = {}
        for i in range(self.board.get_x()):
            for j in range(self.board.get_y()):
                self.states.append((i, j))

        for state in self.states:
            temp = {}
            for action in self.actions:
                temp[action] = 0.1
                self.board.set_cell_score(state, action, temp[action])
            self.Q[state] = temp

        for (i, j, c, w) in self.board.get_specials():
            for action in self.actions:
                self.Q[(i, j)][action] = w
                self.board.set_cell_score((i, j), action, w)

    def do_action(self, action):
        s = self.board.get_player()
        r = -self.board.get_score()
        if action == self.actions[0]:
            (dx, dy, new_action) = self.action_chooser.execute(0)
            self.board.try_move(dx, dy)
        elif action == self.actions[1]:
            (dx, dy, new_action) = self.action_chooser.execute(1)
            self.board.try_move(dx, dy)
        elif action == self.actions[2]:
            (dx, dy, new_action) = self.action_chooser.execute(2)
            self.board.try_move(dx, dy)
        elif action == self.actions[3]:
            (dx, dy, new_action) = self.action_chooser.execute(3)
            self.board.try_move(dx, dy)
        else:
            return
        s2 = self.board.get_player()
        r += self.board.get_score()
        return s, new_action, r, s2

    def max_Q(self, s):
        val = None
        act = None
        for a, q in self.Q[s].items():
            if val is None or (q > val):
                val = q
                act = a
        return act, val

    def inc_Q(self, s, a, alpha, inc):
        self.Q[s][a] *= 1 - alpha
        self.Q[s][a] += alpha * inc
        self.board.set_cell_score(s, a, self.Q[s][a])

    def run(self):
        time.sleep(1)
        t = 1
        while True:
            # Pick the right action
            s = self.board.get_player()
            max_act, max_val = self.max_Q(s)
            (s, a, r, s2) = self.do_action(max_act)
            print("New score " + str(self.board.score))
            print("Try Move to: " + str(max_act))
            print("Move to: " + str(a))

            # Update Q
            max_act, max_val = self.max_Q(s2)
            self.inc_Q(s, a, self.alpha, r * max_val)

            # Check if the game has restarted
            t += 1.0
            if self.board.has_restarted():
                self.board.restart_game()
                time.sleep(0.01)
                t = 1.0

            # Update the learning rate
            self.alpha = pow(t, -0.1)

            # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
            time.sleep(0.1)
