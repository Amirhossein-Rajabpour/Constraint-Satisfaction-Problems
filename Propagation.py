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


# when variables assigned, neighbors add to queue for check domains
def add_neighbors_to_queue(variables_domain, changed_variable, queue):
    x, y = changed_variable[0], changed_variable[1]

    if x >= 1 and variables_domain[x - 1][y] != "0" and variables_domain[x - 1][y] != "1":
        queue.append((x-1, y))
    if x <= len(variables_domain) - 2 and variables_domain[x + 1][y] != "0" and variables_domain[x + 1][y] != "1":
        queue.append((x+1, y))
    if y >= 1 and variables_domain[x][y - 1] != "0" and variables_domain[x][y - 1] != "1":
        queue.append((x, y-1))
    if y <= len(variables_domain) - 2 and variables_domain[x][y + 1] != "0" and variables_domain[x][y + 1] != "1":
        queue.append((x, y+1))


# return new domains arr with Maintaining Arc Consistency (MAC)
def MAC(node):

    board = node.board
    variables_domain = node.variable_domains
    assigned_variable = node.assigned_variable
    queue = [assigned_variable]

    while len(queue) > 0:
        changed_variable = queue.pop(0)
        add_neighbors_to_queue(variables_domain, changed_variable, queue)





