class ValidatePuzzle:

    def execute(self, matrix):
        numbers_list = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                numbers_list.append(int(matrix[i][j]))
        sum = 0
        for position in range(0, len(numbers_list)):
            number = numbers_list[position]
            for i in range(position, len(numbers_list)):
                if number > numbers_list[i] and numbers_list[i] != 0:
                    sum += 1

        if sum % 2 == 0:
            return True
        else:
            return False
