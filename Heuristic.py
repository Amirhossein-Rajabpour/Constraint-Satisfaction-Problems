
def find_minimum_domain(node):
    minimum = 2
    minimum_index = ()
    dimension = len(node.board)
    for i in range(dimension):
        for j in range(dimension):
            if node.board[i][j] == '-' and len(node.variables_domain[i][j]) <= minimum:
                minimum_index = (i,j)
    print(minimum_index)
    return minimum_index

# assigns a value to the selected variable and delete that value from variable's domain
# it returns 0 first and then 1 if zero were removed from domain
def assign_value(node):
    x, y = node.assigned_variable
    if len(node.variables_domain[x][y]) == 0:
        # it means it has no values left
        return '-'
    else:
        new_value = node.variables_domain[x][y].pop()
        if len(node.variables_domain[x][y]) == 0:
            print(node.variables_domain[x][y])
            node.variables_domain[x][y] = new_value
        return new_value

def MRV(node, mode):

    if mode == 'samevar':
        # it means we had conflict in constraint so we need to choose another value for chosen variable
        pass
    else:
        # return variable with the smallest domain
        node.assigned_variable = find_minimum_domain(node)

    # assign a value to this variable
    node.assigned_value = assign_value(node)
    x, y = node.assigned_variable
    node.board[x][y] = node.assigned_value
    print(node.board[x][y])

    # return changed node
    if node.assigned_value != '-':
        return True, node
    else:
        return False, node
