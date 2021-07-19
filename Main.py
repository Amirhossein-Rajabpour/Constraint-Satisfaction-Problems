import CSP


def take_board(filename):
    with open(filename) as file:
        dimension = file.readline()[0]
        puzzle = file.readlines()
        board = []
        for row in puzzle:
            board.append(row.replace('1\n', '1').replace('0\n', '0').replace('-\n', '-').split(' '))
        return board


if __name__ == "__main__":
    file_name = './puzzles/puzzle0.txt'
    board = take_board(file_name)

    const_prop_mode = 'forward_checking'
    CSP.start_CSP(board, const_prop_mode)
