# TODO takes MRV mode

# TODO choose which element of variables domain? for example choose 0 first (then 0 should be removed from variabls domain)

import Heuristic
import Propagation
import Node

def is_end(node):
    pass

def find_path(node):
    path = ''
    return path

assignment = []
# it takes raw input and create basic structures for the program
def start_CSP(input_board, const_prop_mode):
    # TODO create domains dict
    initial_node = Node(input_board, None)  # initial node does not have parent
    domains_dict = {}
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