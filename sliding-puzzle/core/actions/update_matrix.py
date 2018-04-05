from core.services.search_free_position import SearchFreePosition


class UpdateMatrix:

    def execute(self, matrix, movement):

        global edited_matrix

        if len(matrix) == 3:
            edited_matrix = [['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']]
            for i in range(0, 3):
                for j in range(0, 3):
                    edited_matrix[i][j] = matrix[i][j]
        if len(matrix) == 4:
            edited_matrix = [['-1', '-1', '-1', '-1'], ['-1', '-1', '-1', '-1'], ['-1', '-1', '-1', '-1'],
                             ['-1', '-1', '-1', '-1']]
            for i in range(0, 4):
                for j in range(0, 4):
                    edited_matrix[i][j] = matrix[i][j]

        free_position_row = SearchFreePosition().matrix_row(edited_matrix)
        free_position_column = SearchFreePosition().matrix_column(edited_matrix)
        if movement == 'up':
            new_free_position_row = free_position_row - 1
            new_free_position_column = free_position_column
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'right':
            new_free_position_row = free_position_row
            new_free_position_column = free_position_column + 1
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'down':
            new_free_position_row = free_position_row + 1
            new_free_position_column = free_position_column
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        elif movement == 'left':
            new_free_position_row = free_position_row
            new_free_position_column = free_position_column - 1
            aux = edited_matrix[new_free_position_row][new_free_position_column]
            edited_matrix[new_free_position_row][new_free_position_column] = '0'
            edited_matrix[free_position_row][free_position_column] = aux
        return edited_matrix
