from core.services.search_free_position import SearchFreePosition


class GetPossibleMovements:

    def execute(self, matrix):

        free_position_row = SearchFreePosition().matrix_row(matrix)
        free_position_column = SearchFreePosition().matrix_column(matrix)
        movements_list = None

        movements_list = self.when_column_is_in_initial(free_position_column, free_position_row, matrix, movements_list)
        movements_list = self.when_column_is_in_middle(free_position_column, free_position_row, matrix, movements_list)
        movements_list = self.when_column_is_in_last(free_position_column, free_position_row, matrix, movements_list)

        return movements_list

    def when_column_is_in_initial(self, free_position_column, free_position_row, matrix, movements_list):
        if self.initial_row(free_position_row) and self.initial_column(free_position_column):
            movements_list = ['right', 'down']
        elif self.middle_row(matrix, free_position_row) and self.initial_column(free_position_column):
            movements_list = ['up', 'right', 'down']
        elif self.last_row(matrix, free_position_row) and self.initial_column(free_position_column):
            movements_list = ['up', 'right']

        return movements_list

    def when_column_is_in_middle(self, free_position_column, free_position_row, matrix, movements_list):
        if self.initial_row(free_position_row) and self.middle_column(matrix, free_position_column):
            movements_list = ['right', 'down', 'left']
        elif self.middle_row(matrix, free_position_row) and self.middle_column(matrix, free_position_column):
            movements_list = ['up', 'right', 'down', 'left']
        elif self.last_row(matrix, free_position_row) and self.middle_column(matrix, free_position_column):
            movements_list = ['up', 'right', 'left']

        return movements_list

    def when_column_is_in_last(self, free_position_column, free_position_row, matrix, movements_list):
        if self.initial_row(free_position_row) and self.last_column(matrix, free_position_column):
            movements_list = ['down', 'left']
        elif self.middle_row(matrix, free_position_row) and self.last_column(matrix, free_position_column):
            movements_list = ['up', 'down', 'left']
        elif self.last_row(matrix, free_position_row) and self.last_column(matrix, free_position_column):
            movements_list = ['up', 'left']

        return movements_list

    def initial_row(self, free_position_row):
        return free_position_row == 0

    def middle_row(self, matrix, free_position_row):
        return 0 < free_position_row < len(matrix) - 1

    def last_row(self, matrix, free_position_row):
        return free_position_row == len(matrix) - 1

    def initial_column(self, free_position_column):
        return free_position_column == 0

    def middle_column(self, matrix, free_position_column):
        return len(matrix) - 1 > free_position_column > 0

    def last_column(self, matrix, free_position_column):
        return free_position_column == len(matrix) - 1
