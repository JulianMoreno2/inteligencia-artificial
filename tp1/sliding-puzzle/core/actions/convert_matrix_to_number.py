class ConvertMatrixToNumber:

    def execute(self, matrix):
        number_str = ''
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                number_str += matrix[i][j]
        item = int(number_str)
        return item
