
def find_minimum_domain(node):
    minimum = 2
    minimum_index = ()
    dimension = len(node.board)
    for i in range(dimension):
        for j in range(dimension):
            if node.board[i][j] == '-' and len(node.variables_domain[i][j]) <= minimum:
                minimum_index = (i,j)
    return minimum_index

# assigns a value to the selected variable and delete that value from variable's domain
# it returns 0 first and then 1 if zero were removed from domain
def assign_value(node):
    x, y = node.assigned_variable
    if '0' in node.variable_domains[x][y]:
        return '0'
    elif '1' in node.variable_domains[x][y]:
        return '1'
    else:
        'empty'

def MRV(node):
    # return variable with the smallest domain
    node.assigned_variable = find_minimum_domain(node)

    # assign a value to this variable
    node.assigned_value = assign_value(node)

    # return changed node
    if node.assigned_value != 'empty':
        return True, node
    else:
        return False, None
