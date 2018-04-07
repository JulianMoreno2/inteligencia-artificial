from core.actions.convert_input_in_list import ConvertInputInList
from core.actions.create_matrix_from_input import CreateMatrixFromInput
from core.actions.get_puzzle_solution import GetPuzzleSolution
from core.actions.print_matrix import PrintMatrix


class MainPresenter:

    def on_enter_input(self, input):
        list = ConvertInputInList().execute(input)
        matrix = CreateMatrixFromInput().execute(list)

        solution = GetPuzzleSolution().execute(matrix)

        self.print_puzzle_solution(solution)

    def print_puzzle_solution(self, solution):

        matrixs = []
        movements = []

        if solution != None:
            matrixs.append(solution.get_numbers_matrix())
            movements.append(solution.get_last_movement())

            solution_node_parent = solution.get_node_parent()
            while solution_node_parent != None:
                matrixs.append(solution_node_parent.get_numbers_matrix())
                movements.append(solution_node_parent.get_last_movement())
                solution_node_parent = solution_node_parent.get_node_parent()

            movements.pop()
            matrixs.reverse()
            movements.reverse()

            self.print_original_matrix(matrixs)
            self.print_solution_with_movements(matrixs, movements)

        else:
            print('Sorry! This puzzle has no solution.')

        print("Total moves: " + str(len(movements)))

    def print_original_matrix(self, matrixs):
        PrintMatrix().execute(matrixs[0])

    def print_solution_with_movements(self, matrixs, movements):
        for i in range(1, len(matrixs)):
            print(str(i) + ") Movement: " + movements[i - 1])
            PrintMatrix().execute(matrixs[i])
