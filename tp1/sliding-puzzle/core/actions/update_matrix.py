from core.services.search_free_position import SearchFreePosition


class UpdateMatrix:

    def execute(self, matrix, movement):

        initialized_matrix = self.initialize_matrix(matrix)

        free_row = SearchFreePosition().matrix_row(initialized_matrix)
        free_column = SearchFreePosition().matrix_column(initialized_matrix)
        new_free_row = free_row
        new_free_column = free_column

        if movement == 'up':
            new_free_row = free_row - 1
            new_free_column = free_column
        elif movement == 'right':
            new_free_row = free_row
            new_free_column = free_column + 1
        elif movement == 'down':
            new_free_row = free_row + 1
            new_free_column = free_column
        elif movement == 'left':
            new_free_row = free_row
            new_free_column = free_column - 1

        self.update(initialized_matrix, free_column, free_row, new_free_column, new_free_row)

        return initialized_matrix

    def initialize_matrix(self, matrix):
        if len(matrix) == 3:
            return self.initialize_3_by_3_matrix(matrix)
        if len(matrix) == 4:
            return self.initialize_4_by_4_matrix(matrix)

    def initialize_3_by_3_matrix(self, matrix):
        if len(matrix) == 3:
            initialized_matrix = [['0', '0', '0'],
                                  ['0', '0', '0'],
                                  ['0', '0', '0']]
            for i in range(0, 3):
                for j in range(0, 3):
                    initialized_matrix[i][j] = matrix[i][j]

            return initialized_matrix

    def initialize_4_by_4_matrix(self, matrix):
        if len(matrix) == 4:
            initialized_matrix = [['0', '0', '0', '0'],
                                  ['0', '0', '0', '0'],
                                  ['0', '0', '0', '0'],
                                  ['0', '0', '0', '0']]
            for i in range(0, 4):
                for j in range(0, 4):
                    initialized_matrix[i][j] = matrix[i][j]

            return initialized_matrix

    def update(self, matrix, free_column, free_row, new_free_column, new_free_row):
        old_value = matrix[new_free_row][new_free_column]
        matrix[new_free_row][new_free_column] = '0'
        matrix[free_row][free_column] = old_value
