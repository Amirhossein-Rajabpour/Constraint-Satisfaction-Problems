class Node:
    def __init__(self, board, parent, variable_domains, assigned_variable, assigned_value):
        self.board = board
        self.parent = parent
        self.variable_domains = variable_domains
        self.assigned_variable = assigned_variable
        self.assigned_value = assigned_value
