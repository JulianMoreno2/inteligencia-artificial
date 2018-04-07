from core.actions.update_matrix import UpdateMatrix
from core.actions.convert_matrix_to_number import ConvertMatrixToNumber
from core.actions.get_possible_movements import GetPossibleMovements
from core.actions.validate_puzzle import ValidatePuzzle
from core.actions.verify_puzzle_is_solution import VerifyPuzzleIsSolution
from core.domain.node import Node


class GetPuzzleSolution:

    def execute(self, matrix):

        explored_nodes = {}
        solution_node = None

        if ValidatePuzzle().execute(matrix):

            initial_node = Node(None, matrix, None)

            frontier_nodes = []
            explored_nodes[ConvertMatrixToNumber().execute(initial_node.get_numbers_matrix())] = 1
            frontier_nodes.insert(0, initial_node)

            while len(frontier_nodes) > 0 and solution_node is None:

                current_node = frontier_nodes.pop()
                current_node_matrix = current_node.get_numbers_matrix()
                explored_nodes[ConvertMatrixToNumber().execute(current_node_matrix)] = 1

                if not VerifyPuzzleIsSolution().execute(current_node_matrix):
                    movements_list = GetPossibleMovements().execute(current_node_matrix)

                    for movement in movements_list:
                        updated_matrix = UpdateMatrix().execute(current_node_matrix, movement)
                        explored_node = False
                        updated_matrix_id = ConvertMatrixToNumber().execute(updated_matrix)

                        if updated_matrix_id in explored_nodes:
                            explored_node = True
                        if not explored_node:
                            new_node = Node(current_node, updated_matrix, movement)
                            frontier_nodes.insert(0, new_node)
                else:
                    solution_node = current_node

        return solution_node
