import copy

from GameRule import *


# return new domains arr with forward checking
def forward_checking(variables_domain):
    # board = node.board
    # variables_domain = node.variables_domain
    flag = True
    variables_domain_copy = copy.deepcopy(variables_domain)
    # print("ghable forwardddd")
    # print("var domains")
    # print(variables_domain_copy)
    # print("-----------------------------")

    for i in range(len(variables_domain_copy)):
        for j in range(len(variables_domain_copy)):
            if variables_domain_copy[i][j] != "0" and variables_domain_copy[i][j] != "1":
                variable_index = (i, j)
                print("in index ", variable_index)
                flag, new_variables_domain = check_variables_domains_with_rule_game(variables_domain_copy,
                                                                                    variable_index)
                if flag:
                    variables_domain_copy = new_variables_domain
                else:
                    break

        if not flag:
            break

    # when all variables domain aren't empty
    if flag:
        return True, variables_domain_copy

    # when at least one variable domain is empty
    else:
        return False, []


def is_change_domain(variables_domain, variable_index):
    x, y = variable_index[0], variable_index[1]
    prev_variable_domain = variables_domain[x][y]
    flag, new_variables_domain = check_variables_domains_with_rule_game(variables_domain, variable_index)
    if flag:
        new_variable_domain = new_variables_domain[x][y]
        if new_variable_domain != prev_variable_domain:  # when variable domain changed => added to queue
            return True, new_variables_domain
        else:
            return False, new_variables_domain  # variable domain isn't changed => not added to queue
    else:
        return False, []


# when variables assigned, neighbors add to queue for check domains
def add_neighbors_to_queue(variables_domain, changed_variable, queue):
    x, y = changed_variable[0], changed_variable[1]
    new_variables_domain = []

    if x >= 1 and variables_domain[x - 1][y] != "0" and variables_domain[x - 1][y] != "1":
        is_changed_domain, new_variables_domain = is_change_domain(variables_domain, changed_variable)
        if is_changed_domain:
            queue.append((x - 1, y))
        if not new_variables_domain:
            return False  # backtracking

    if x <= len(variables_domain) - 2 and variables_domain[x + 1][y] != "0" and variables_domain[x + 1][y] != "1":
        is_changed_domain, new_variables_domain = is_change_domain(new_variables_domain, changed_variable)
        if is_changed_domain:
            queue.append((x + 1, y))
        if not new_variables_domain:
            return False, False  # backtracking

    if y >= 1 and variables_domain[x][y - 1] != "0" and variables_domain[x][y - 1] != "1":
        is_changed_domain, new_variables_domain = is_change_domain(new_variables_domain, changed_variable)
        if is_changed_domain:
            queue.append((x, y - 1))
        if not new_variables_domain:
            return False, False

    if y <= len(variables_domain) - 2 and variables_domain[x][y + 1] != "0" and variables_domain[x][y + 1] != "1":
        is_changed_domain, new_variables_domain = is_change_domain(new_variables_domain, changed_variable)
        if is_changed_domain:
            queue.append((x, y + 1))
        if not new_variables_domain:
            return False, False

    return True, new_variables_domain


# return new domains arr with Maintaining Arc Consistency (MAC)
def MAC(node):
    board = node.board
    variables_domain = node.variables_domain
    assigned_variable = node.assigned_variable
    queue = [assigned_variable]
    flag = True

    while len(queue) > 0:
        changed_variable = queue.pop(0)
        flag, new_variables_domain = add_neighbors_to_queue(variables_domain, changed_variable, queue)
        if not flag:
            break

    if flag:
        return True, new_variables_domain
    else:
        return False, []
