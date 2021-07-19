from GameRule import *

# they return new domains dictionary

def forward_checking(node):
    board = node.board
    variables_domain = node.variables_domain

    for i in range(len(board)):
        for j in range(len(board[0])):
            if variables_domain[i, j] != "0" and variables_domain[i, j] != "1":


