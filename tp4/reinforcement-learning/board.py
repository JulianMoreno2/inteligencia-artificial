try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class Board:

    def __init__(self, size, walk_reward, lose_reward, win_reward):
        self.master = Tk()

        self.triangle_size = 0.1
        self.cell_score_min = -0.2
        self.cell_score_max = 0.2
        self.width = 100
        (self.x, self.y) = (size, size)
        self.actions = ["up", "down", "left", "right"]

        self.board = Canvas(self.master, width=self.x * self.width, height=self.y * self.width)
        self.player = (0, 0)
        self.score = 0
        self.restart = False
        self.walk_reward = walk_reward
        self.me = None

        self.specials = []
        for i in range(1, size - 1):
            self.specials.append((i, 0, "red", lose_reward))
        self.specials.append((size - 1, 0, "green", win_reward))

        self.cell_scores = {}

    def create_triangle(self, i, j, action):
        if action == self.actions[0]:
            return self.board.create_polygon((i + 0.5 - self.triangle_size) * self.width,
                                             (j + self.triangle_size) * self.width,
                                             (i + 0.5 + self.triangle_size) * self.width,
                                             (j + self.triangle_size) * self.width,
                                             (i + 0.5) * self.width, j * self.width,
                                             fill="white", width=1)
        elif action == self.actions[1]:
            return self.board.create_polygon((i + 0.5 - self.triangle_size) * self.width,
                                             (j + 1 - self.triangle_size) * self.width,
                                             (i + 0.5 + self.triangle_size) * self.width,
                                             (j + 1 - self.triangle_size) * self.width,
                                             (i + 0.5) * self.width, (j + 1) * self.width,
                                             fill="white", width=1)
        elif action == self.actions[2]:
            return self.board.create_polygon((i + self.triangle_size) * self.width,
                                             (j + 0.5 - self.triangle_size) * self.width,
                                             (i + self.triangle_size) * self.width,
                                             (j + 0.5 + self.triangle_size) * self.width,
                                             i * self.width, (j + 0.5) * self.width,
                                             fill="white", width=1)
        elif action == self.actions[3]:
            return self.board.create_polygon((i + 1 - self.triangle_size) * self.width,
                                             (j + 0.5 - self.triangle_size) * self.width,
                                             (i + 1 - self.triangle_size) * self.width,
                                             (j + 0.5 + self.triangle_size) * self.width,
                                             (i + 1) * self.width, (j + 0.5) * self.width,
                                             fill="white", width=1)

    def render_grid(self):

        for i in range(self.x):
            for j in range(self.y):
                self.board.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width, fill="white", width=1)

        for (i, j, c, w) in self.specials:
            self.board.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width, fill=c, width=1)

        for i in range(self.x):
            for j in range(self.y):
                temp = {}
                for action in self.actions:
                    temp[action] = self.create_triangle(i, j, action)
                self.cell_scores[(i, j)] = temp

    def set_cell_score(self, state, action, val):
        triangle = self.cell_scores[state][action]
        green_dec = int(min(255, max(0, (val - self.cell_score_min) * 255.0 / (self.cell_score_max - self.cell_score_min))))
        green = hex(green_dec)[2:]
        red = hex(255 - green_dec)[2:]
        if len(red) == 1:
            red += "0"
        if len(green) == 1:
            green += "0"
        color = "#" + red + green + "00"
        self.board.itemconfigure(triangle, fill=color)

    def try_move(self, dx, dy):
        if self.restart:
            self.restart_game()
        new_x = self.player[0] + dx
        new_y = self.player[1] + dy
        self.score += self.walk_reward
        if (new_x >= 0) and (new_x < self.x) and (new_y >= 0) and (new_y < self.y):
            self.board.coords(self.me,
                              new_x * self.width + self.width * 2 / 10,
                              new_y * self.width + self.width * 2 / 10,
                              new_x * self.width + self.width * 8 / 10,
                              new_y * self.width + self.width * 8 / 10)
            self.player = (new_x, new_y)
        for (i, j, c, w) in self.specials:
            if new_x == i and new_y == j:
                self.score -= self.walk_reward
                self.score += w
                if c == "green":
                    print("Finish with score: ", self.score)
                    self.restart = True
                return

    def call_up(self):
        self.try_move(0, -1)

    def call_down(self):
        self.try_move(0, 1)

    def call_left(self):
        self.try_move(-1, 0)

    def call_right(self):
        self.try_move(1, 0)

    def restart_game(self):
        self.player = (0, 0)
        self.score = 1
        self.restart = False
        self.board.coords(self.me,
                          self.player[0] * self.width + self.width * 2 / 10,
                          self.player[1] * self.width + self.width * 2 / 10,
                          self.player[0] * self.width + self.width * 8 / 10,
                          self.player[1] * self.width + self.width * 8 / 10)

    def has_restarted(self):
        return self.restart

    def start_game(self):
        print("Start game")
        self.master.bind("<Up>", self.call_up)
        self.master.bind("<Down>", self.call_down)
        self.master.bind("<Right>", self.call_right)
        self.master.bind("<Left>", self.call_left)

        self.me = self.board.create_rectangle(self.player[0] * self.width + self.width * 2 / 10,
                                              self.player[1] * self.width + self.width * 2 / 10,
                                              self.player[0] * self.width + self.width * 8 / 10,
                                              self.player[1] * self.width + self.width * 8 / 10,
                                              fill="black", width=1, tag="me")

        self.board.grid(row=0, column=0)
        self.master.mainloop()

    def get_specials(self):
        return self.specials

    def get_actions(self):
        return self.actions

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_player(self):
        return self.player

    def get_score(self):
        return self.score
