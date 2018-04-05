from core.actions.convert_input_in_list import ConvertInputInList
from core.actions.create_matrix_from_input import CreateMatrixFromInput
from core.actions.get_puzzle_solution import GetPuzzleSolution
from core.actions.print_matrix import PrintMatrix


class MainPresenter:

    def on_enter_input(self, input):
        list = ConvertInputInList().execute(input)
        matrix = CreateMatrixFromInput().execute(list)

        solution = GetPuzzleSolution().execute(matrix)
        solution_node = solution[0]
        explored_nodes = solution[1]

        self.print_puzzle_solution(solution_node, explored_nodes)

    def print_puzzle_solution(self, solution_node, explored_nodes):

        parents_matrix_list = []
        parents_movement_list = []

        if solution_node != None:
            parents_matrix_list.append(solution_node.get_numbers_matrix())
            parents_movement_list.append(solution_node.get_last_movement())

            solution_node_parent = solution_node.get_node_parent()
            while solution_node_parent != None:
                parents_matrix_list.append(solution_node_parent.get_numbers_matrix())
                parents_movement_list.append(solution_node_parent.get_last_movement())
                solution_node_parent = solution_node_parent.get_node_parent()

            parents_movement_list.pop()
            parents_matrix_list.reverse()
            parents_movement_list.reverse()

            self.print_original_matrix(parents_matrix_list)
            self.print_matrix_solution_with_movements(parents_matrix_list, parents_movement_list)

        else:
            print('Sorry! This puzzle has no solution.')

        print("Total moves: " + str(len(parents_movement_list)))
        print("Total evaluated nodes: " + str(len(explored_nodes)))

    def print_original_matrix(self, parents_matrix_list):
        PrintMatrix().execute(parents_matrix_list[0])

    def print_matrix_solution_with_movements(self, parents_matrix_list, parents_movement_list):
        for i in range(1, len(parents_matrix_list)):
            print(str(i) + ") Movement: " + parents_movement_list[i - 1])
            PrintMatrix().execute(parents_matrix_list[i])
