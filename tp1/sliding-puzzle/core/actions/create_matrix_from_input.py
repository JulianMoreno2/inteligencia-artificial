class CreateMatrixFromInput:

    def execute(self, list):
        if len(list) == 9:
            return self.create_three_by_three_matrix(list)
        if len(list) == 16:
            return self.create_four_by_four_matrix(list)
        else:
            print("The amount of numbers must be 9 or 16")

    def create_three_by_three_matrix(self, list):
        three_by_three_matrix = [[], [], []]
        current_number = 1
        for number in list:
            if current_number <= 3:
                three_by_three_matrix[0].append(number)
                current_number += 1
            elif current_number <= 6:
                three_by_three_matrix[1].append(number)
                current_number += 1
            elif current_number <= 9:
                three_by_three_matrix[2].append(number)
                current_number += 1
        return three_by_three_matrix

    def create_four_by_four_matrix(self, list):
        four_by_four_matrix = [[], [], [], []]
        current_number = 1
        for number in list:
            if current_number <= 4:
                four_by_four_matrix[0].append(number)
                current_number += 1
            elif current_number <= 8:
                four_by_four_matrix[1].append(number)
                current_number += 1
            elif current_number <= 12:
                four_by_four_matrix[2].append(number)
                current_number += 1
            elif current_number <= 16:
                four_by_four_matrix[3].append(number)
                current_number += 1
        return four_by_four_matrix
