class VerifyPuzzleIsSolution:

    def execute(self, matrix):

        if len(matrix) == 3:
            three_by_three_solution = [['0', '1', '2'],
                                       ['3', '4', '5'],
                                       ['6', '7', '8']]
            return matrix == three_by_three_solution

        if len(matrix) == 4:
            four_by_four_solution = [['0', '1', '2', '3'],
                                     ['4', '5', '6', '7'],
                                     ['8', '9', '10', '11'],
                                     ['12', '13', '14', '15']]
            return matrix == four_by_four_solution

        return False
