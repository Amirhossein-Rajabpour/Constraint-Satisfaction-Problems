# import CSP

def take_board(file):

    dimension = f.readline()[0]
    puzzle = f.readlines()
    board = []
    for row in puzzle:
        board.append(row.replace('1\n', '1').replace('0\n', '0').replace('-\n', '-').split(' '))
    return board

if __name__ == '__main__':

    file_name = 'puzzles/puzzle0.txt'
    f = open(file_name, "r")
    board = take_board(f)
    print(board)

    const_prop_mode = 'forwardchecking'
    # CSP.start_CSP(board, const_prop_mode)