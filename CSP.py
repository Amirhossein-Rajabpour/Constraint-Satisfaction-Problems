import Heuristic
import Propagation
import Node
import copy


def find_path(node):
    path = ''
    return path


def create_domains_list(initial_board):
    domains_list = copy.deepcopy(initial_board)
    dimension, _ = len(domains_list)

    for i in range(dimension):
        for j in range(dimension):
            if domains_list[i][j] == '1':
                domains_list[i][j] = '1'
            elif domains_list[i][j] == '0':
                domains_list[i][j] = '0'
            else:
                domains_list[i][j] = ['0', '1']

    return domains_list


# it takes raw input and create basic structures for the program
def start_CSP(input_board, const_prop_mode):

    domains_list = create_domains_list(input_board)
    initial_node = Node.Node(input_board, '', domains_list, '', '')  # initial node does not have parent
    CSP_Backtracking(initial_node, const_prop_mode)


def CSP_Backtracking(node, const_prop_mode):

    while True:
        not_empty, node = Heuristic.MRV(node)
        print(node.board)
        if not not_empty:
            # here we should go to parent node
            CSP_Backtracking(node.parent, const_prop_mode)
        else:
            if const_prop_mode == 'forwardchecking':
                state, variable_domains = Propagation.forward_checking(node)
            elif const_prop_mode == 'MAC':
                state, variable_domains = Propagation.MAC(node)

            if state:
                # continue solving the puzzle
                child_node = Node.Node(node.board, node, variable_domains, '', '')
                CSP_Backtracking(child_node, const_prop_mode)
            else:
                # new values for assigned_variable should be considered
                CSP_Backtracking(node, const_prop_mode)


        # if not is_end(assignment[-1]):
        #     CSP_Backtracking(domains_list, const_prop_mode)
        # else:
        #     # find path takes answer node as input
        #     path = find_path(assignment[-1])
        #     return path