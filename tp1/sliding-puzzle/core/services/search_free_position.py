class SearchFreePosition:

    def matrix_row(self, matrix):
        free_position_row = -1
        for current_row in range(0, len(matrix)):
            for number in matrix[current_row]:
                if number == '0':
                    free_position_row = current_row
                    break
        return free_position_row

    def matrix_column(self, matrix):
        free_position_column = -1
        for current_row in range(0, len(matrix)):
            position = 0
            for number in matrix[current_row]:
                if number == '0':
                    free_position_column = position
                    break
                position += 1
        return free_position_column
