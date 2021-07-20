import Heuristic
import Propagation
import Node
import copy
import GameRule
import sys

sys.setrecursionlimit(10 ** 6)


def print_board(node):
    print(f'value {node.assigned_value} assigned to index {node.assigned_variable}\n')
    for i in node.board:
        print(i)
    print('*******************************************')


def create_domains_list(initial_board):
    domains_list = copy.deepcopy(initial_board)
    dimension = len(domains_list)

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
    CSP_Backtracking(initial_node, const_prop_mode, 'start')


def CSP_Backtracking(node, const_prop_mode, csp_mode):

    is_finished = GameRule.check_all_rule_game(node)
    if is_finished:
        print('finish')
        print_board(node)
        return

    print('before MRV')
    for i in node.board:
        print(i)
    not_empty, node = Heuristic.MRV(node, csp_mode)
    print_board(node)
    if not not_empty:
        # here we should go to parent node
        print('back to parent')
        CSP_Backtracking(node.parent, const_prop_mode, 'continue')
    else:
        if const_prop_mode == 'forward_checking':
            variables_domain_copy = copy.deepcopy(node.variables_domain)
            variables_domain_copy[node.assigned_variable[0]][node.assigned_variable[1]] = node.assigned_value
            flag, variables_domain = Propagation.forward_checking(variables_domain_copy)
            print('after FC: ', node.variables_domain)
        elif const_prop_mode == 'MAC':
            flag, variables_domain = Propagation.MAC(node)

        if flag:
            # continue solving the puzzle
            print('continue')
            board_copy = copy.deepcopy(node.board)
            child_node = Node.Node(board_copy, node, variables_domain, '', '')
            CSP_Backtracking(child_node, const_prop_mode, 'continue')
        elif not flag and len(node.variables_domain[node.assigned_variable[0]][node.assigned_variable[1]]) == 0:
            # backtracking
            print('domain is empty. we should backtrack')
            CSP_Backtracking(node.parent, const_prop_mode, 'backtracking')
        else:
            # new values for assigned_variable should be considered
            print('change last variable value')
            CSP_Backtracking(node, const_prop_mode, 'samevar')