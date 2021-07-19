# TODO takes MRV mode

# TODO choose which element of variables domain? for example choose 0 first (then 0 should be removed from variabls domain)

import Heuristic
import Propagation
import Node
import math

assignment = []

def is_end(node):
    pass

def find_path(node):
    path = ''
    return path

def create_domains_dict(initial_board, dimension):
    domains_dict = {}
    dimension = int(dimension)
    for i in range(1, (dimension**2)+1):
        x = math.ceil(i/dimension) - 1
        y = (i % dimension) - 1
        if initial_board[x][y] == '1' or initial_board[x][y] == '0':
            domains_dict[i] = []
        else:
            domains_dict[i] = ['0', '1']
    return domains_dict


# it takes raw input and create basic structures for the program
def start_CSP(input_board, dimension, const_prop_mode):
    # TODO create domains dict
    initial_node = Node.Node(input_board, '')  # initial node does not have parent
    domains_dict = create_domains_dict(input_board, dimension)
    assignment.append(initial_node)
    CSP_Backtracking(domains_dict, const_prop_mode)

def CSP_Backtracking(domains_dict, const_prop_mode):

    while True:
        cell = Heuristic.MRV(domains_dict)
        assignment.append(cell)
        if const_prop_mode == 'forwardchecking':
            domains_dict = Propagation.forwardchecking(cell, assignment)    # cell is the last element of assignment array i guess
        elif const_prop_mode == 'MAC':
            domains_dict = Propagation.MAC(cell, assignment)    # cell is the last element of assignment array i guess

        if not is_end(assignment[-1]):
            CSP_Backtracking(domains_dict, const_prop_mode)
        else:
            # find path takes answer node as input
            path = find_path(assignment[-1])
            # not sure to return path or final node!
            return path