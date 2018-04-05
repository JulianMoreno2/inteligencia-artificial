class VerifyPuzzleIsSolution:

    def execute(self, matrix):
        solution = False
        if len(matrix) == 3:
            if matrix == [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]:
                solution = True
        elif len(matrix) == 4:
            if matrix == [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]:
                solution = True
        return solution
