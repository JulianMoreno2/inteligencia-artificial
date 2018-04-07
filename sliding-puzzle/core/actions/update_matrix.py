from core.services.search_free_position import SearchFreePosition


class UpdateMatrix:

    def execute(self, matrix, movement):

        global edited_matrix

        if len(matrix) == 3:
            edited_matrix = [['-1', '-1', '-1'],
                             ['-1', '-1', '-1'],
                             ['-1', '-1', '-1']]
            for i in range(0, 3):
                for j in range(0, 3):
                    edited_matrix[i][j] = matrix[i][j]
        if len(matrix) == 4:
            edited_matrix = [['-1', '-1', '-1', '-1'],
                             ['-1', '-1', '-1', '-1'],
                             ['-1', '-1', '-1', '-1'],
                             ['-1', '-1', '-1', '-1']]
            for i in range(0, 4):
                for j in range(0, 4):
                    edited_matrix[i][j] = matrix[i][j]

        free_row = SearchFreePosition().matrix_row(edited_matrix)
        free_column = SearchFreePosition().matrix_column(edited_matrix)

        if movement == 'up':
            new_free_row = free_row - 1
            new_free_column = free_column
            self.update(edited_matrix, free_column, free_row, new_free_column, new_free_row)
        elif movement == 'right':
            new_free_row = free_row
            new_free_column = free_column + 1
            self.update(edited_matrix, free_column, free_row, new_free_column, new_free_row)
        elif movement == 'down':
            new_free_row = free_row + 1
            new_free_column = free_column
            self.update(edited_matrix, free_column, free_row, new_free_column, new_free_row)
        elif movement == 'left':
            new_free_row = free_row
            new_free_column = free_column - 1
            self.update(edited_matrix, free_column, free_row, new_free_column, new_free_row)

        return edited_matrix

    def update(self, edited_matrix, free_column, free_row, new_free_column, new_free_row):
        old_value = edited_matrix[new_free_row][new_free_column]
        edited_matrix[new_free_row][new_free_column] = '0'
        edited_matrix[free_row][free_column] = old_value
