import CSP
import time


def take_board(filename):
    with open(filename) as file:
        dimension = file.readline()[0]
        puzzle = file.readlines()
        board = []
        for row in puzzle:
            board.append(row.replace('1\n', '1').replace('0\n', '0').replace('-\n', '-').split(' '))
        return board


if __name__ == "__main__":
    file_name = './puzzles/puzzle3.txt'
    board = take_board(file_name)

    starting_time = time.time()
    const_prop_mode = "MAC"
    CSP.start_CSP(board, const_prop_mode)
    ending_time = time.time()
    duration = ending_time - starting_time
    print("\n\nTime analysis")
    print(f'for constraint propagation {const_prop_mode} took {duration} secs long')