from GameRule import *


# return new domains arr with forward checking
def forward_checking(node):
    board = node.board
    variables_domain = node.variables_domain
    flag = True

    for i in range(len(board)):
        for j in range(len(board[0])):
            if variables_domain[i, j] != "0" and variables_domain[i, j] != "1":
                variable_index = (i, j)
                flag, new_variables_domain = check_variables_domains_with_rule_game(variables_domain, variable_index)
                if flag:
                    variables_domain = new_variables_domain
                else:
                    break

        if not flag:
            break

    # when all variables domain aren't empty
    if flag:
        return True, variables_domain

    # when at least one variable domain is empty
    else:
        return False, []


# return new domains arr with Maintaining Arc Consistency (MAC)
def MAC(node):
    board = node.board
    variables_domain = node.variable_domains
