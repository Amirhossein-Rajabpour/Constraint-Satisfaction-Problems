import numpy as np


# calculate number of digit in row or column
def calculate_number_of_digit(row_or_column, digit):
    count_digit = np.count_nonzero(row_or_column == digit)
    return count_digit


# check numbers of digit in each row and column
def is_equal_numbers_of_digit(node):
    plate = node.board
    plate_coordinates = {"x": len(plate), "y": len(plate[0])}

    # check rows
    for row in plate:
        if np.count_nonzero(row == "-") == 0:
            if calculate_number_of_digit(row, "0") != calculate_number_of_digit(row, "1"):
                return False

    # check columns
    for i in range(len(plate_coordinates)):
        column = plate[:, i]
        if np.count_nonzero(column == "-") == 0:
            if calculate_number_of_digit(column, "0") != calculate_number_of_digit(column, "1"):
                return False

    return True



def is_unique_string_in_board(node):
