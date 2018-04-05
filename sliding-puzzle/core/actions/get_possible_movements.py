from core.services.search_free_position import SearchFreePosition


class GetPossibleMovements:

    def execute(self, matrix):

        free_position_row = SearchFreePosition().matrix_row(matrix)
        free_position_column = SearchFreePosition().matrix_column(matrix)
        movements_list = None

        movements_list = self.when_column_is_in_initial(free_position_column, free_position_row, matrix, movements_list)
        movements_list = self.when_column_is_in_middle(free_position_column, free_position_row, matrix, movements_list)
        movements_list = self.when_column_in_last(free_position_column, free_position_row, matrix, movements_list)

        return movements_list

    def when_column_is_in_initial(self, free_position_column, free_position_row, matrix, movements_list):
        if free_position_row == 0 and free_position_column == 0:
            movements_list = ['right', 'down']
        elif free_position_row == len(matrix) - 1 and free_position_column == 0:
            movements_list = ['up', 'right']
        elif 0 < free_position_row < len(matrix) - 1 and free_position_column == 0:
            movements_list = ['up', 'right', 'down']
        return movements_list

    def when_column_is_in_middle(self, free_position_column, free_position_row, matrix, movements_list):
        if free_position_row == 0 and len(matrix) - 1 > free_position_column > 0:
            movements_list = ['right', 'down', 'left']
        elif free_position_row == len(matrix) - 1 and len(matrix) - 1 > free_position_column > 0:
            movements_list = ['up', 'right', 'left']
        elif 0 < free_position_row < len(matrix) - 1 and len(matrix) - 1 > free_position_column > 0:
            movements_list = ['up', 'right', 'down', 'left']
        return movements_list

    def when_column_in_last(self, free_position_column, free_position_row, matrix, movements_list):
        if free_position_row == 0 and free_position_column == len(matrix) - 1:
            movements_list = ['down', 'left']
        elif free_position_row == len(matrix) - 1 and free_position_column == len(matrix) - 1:
            movements_list = ['up', 'left']
        elif 0 < free_position_row < len(matrix) - 1 and free_position_column == len(matrix) - 1:
            movements_list = ['up', 'down', 'left']
        return movements_list
