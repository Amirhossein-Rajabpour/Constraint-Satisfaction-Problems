import Heuristic
import Propagation
from Node import *
import copy
from GameRule import *

import sys
sys.setrecursionlimit(10 ** 9)


def print_board(board):
    for i in board:
        print(i)
    print('*******************************************')


def create_domains_list(initial_board):
    domains_list = copy.deepcopy(initial_board)
    dimension = len(domains_list)

    # convert puzzle board to my structure
    # when still value is not assigned to cell,shows in array.
    # when value is assigned to cell, shows with string "0" or "1"
    for i in range(dimension):
        for j in range(dimension):
            if domains_list[i][j] == '1':
                domains_list[i][j] = '1'
            elif domains_list[i][j] == '0':
                domains_list[i][j] = '0'
            else:
                domains_list[i][j] = ['0', '1']

    # check domains with game rules
    for i in range(dimension):
        for j in range(dimension):
            if domains_list[i][j] != "0" and domains_list[i][j] != "1":     # when value is not assigned to variable
                flag, new_domains_list = check_variables_domains_with_rule_game(domains_list, (i, j))

                if flag:
                    domains_list = new_domains_list
                else:
                    return False, []

    return True, domains_list


# check puzzle when is backtracking to base_node, return False (puzzle is unsolvable)
def is_solvable(node):
    if node.board == "":
        print(" ====> This puzzle is unsolvable <====")
        return False

    return True


# it takes raw input and create basic structures for the program
def start_CSP(input_board, const_prop_mode):

    # we start from base_node (base_node is parent of initial_node)
    base_node = Node("", "", "", "", "")
    is_puzzle_solved_with_game_rule, domains_list = create_domains_list(input_board)
    if not is_puzzle_solved_with_game_rule:
        print("This puzzle is breaking game rule")
        return

    initial_node = Node(input_board, base_node, domains_list, '', '')  # initial node have parent => base_node
    CSP_Backtracking(initial_node, const_prop_mode, 'start')


def CSP_Backtracking(node, const_prop_mode, csp_mode):

    # check we arrive to node_base or not (when we arrive to node_base, puzzle is unsolvable)
    if not is_solvable(node):
        return

    is_finished = check_all_rule_game(node)
    if is_finished:
        print('\n\n*************************** SOLVED PUZZLE *************************\n')
        print_board(node.board)
        return

    print("**********************************************************")
    print('***** Before MRV *****')
    print_board(node.board)

    not_empty = Heuristic.MRV(node, csp_mode)

    if not not_empty:
        # here we should go to parent node
        print(" =====> BACKTRACKING <===== ")
        CSP_Backtracking(node.parent, const_prop_mode, 'continue')
    else:
        print("***** After MRV *****")
        new_variables_domain = copy.deepcopy(node.variables_domain)
        x, y = node.assigned_variable
        new_variables_domain[x][y] = node.assigned_value
        new_board = copy.deepcopy(node.board)
        new_board[x][y] = node.assigned_value
        print("(MRV) => assigned variable {} = {}".format(node.assigned_variable, node.assigned_value))
        print_board(new_board)
        print("**********************************************************")

        if const_prop_mode == 'forward-checking':
            # print('var domains node ghable forward:\n')
            # for i in new_variables_domain:
            #     print(i)
            flag, variables_domain = Propagation.forward_checking(new_variables_domain)

            # print("after FC flag is ", flag)
            # print("var domains node after forward: \n")
            # for i in variables_domain:
            #     print(i)
            # print('after FC: ', node.variables_domain)
        elif const_prop_mode == 'MAC':
            flag, variables_domain = Propagation.MAC(new_variables_domain, node.assigned_variable)


        if flag:
            # continue solving the puzzle
            print('***** Continue solving puzzle *****')
            child_node = Node(new_board, node, variables_domain, '', '')
            CSP_Backtracking(child_node, const_prop_mode, 'continue')

        elif not flag and len(node.variables_domain[x][y]) == 0:
            # backtracking
            print('!!! Domain is empty ====> BACKTRACKING')
            # print("node parent variables")
            # print(node.parent.variables_domain)
            CSP_Backtracking(node.parent, const_prop_mode, 'backtracking')

        else:
            # new values for assigned_variable should be considered
            print(" ==> Change last assigned variable value <== ")
            CSP_Backtracking(node, const_prop_mode, 'samevar')
