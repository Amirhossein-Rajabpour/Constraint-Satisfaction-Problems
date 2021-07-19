class Node:
    def __init__(self, board, parent, variables_domain, assigned_variable, assigned_value):
        self.board = board
        self.parent = parent
        self.variables_domain = variables_domain
        self.assigned_variable = assigned_variable
        self.assigned_value = assigned_value
