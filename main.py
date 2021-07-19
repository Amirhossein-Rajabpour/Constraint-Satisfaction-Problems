import numpy as np
import CSP

if __name__ == '__main__':

    file_name = 'puzzles/puzzle0.txt'
    f = open(file_name, "r")
    dimension = f.readline()[0]
    puzzle = f.readlines()
    # for row in puzzle: print(row[0])
    board = []
    for row in puzzle:
        n_row = row.replace('1\n', '1').replace('0\n', '0').replace('-\n', '-').split(' ')
        board.append(n_row)
    board = np.array(board)

    const_prop_mode = 'forwardchecking'
    CSP.start_CSP(board, const_prop_mode)