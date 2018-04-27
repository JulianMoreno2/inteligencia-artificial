class Node:
    node_parent = None
    matrix = None
    last_movement = None

    def __init__(self, node_parent, matrix, last_movement):
        self.node_parent = node_parent
        self.matrix = matrix
        self.last_movement = last_movement

    def get_node_parent(self):
        return self.node_parent

    def get_matrix(self):
        return self.matrix

    def get_last_movement(self):
        return self.last_movement
