import numpy as np


# calculate number of digit in row or column
def calculate_number_of_digit(row_or_column, digit):
    count_digit = np.count_nonzero(row_or_column == digit)
    return count_digit


# check numbers of digit in each row and column
def is_equal_numbers_of_digit(node):
    board = node.board

    # check rows
    for row in board:
        if np.count_nonzero(row == "-") == 0:
            if calculate_number_of_digit(row, "0") != calculate_number_of_digit(row, "1"):
                return False

    # check columns
    for i in range(len(board)):
        column = board[:, i]
        if np.count_nonzero(column == "-") == 0:
            if calculate_number_of_digit(column, "0") != calculate_number_of_digit(column, "1"):
                return False

    return True


# combine char to created string
def created_string_with_char(char_arr):
    created_string = ""
    for char in char_arr:
        created_string += char

    return created_string


# check unique strings in rows or columns
def check_unique_strings(strings_arr_in_rows_or_columns):
    unique, counts = np.unique(strings_arr_in_rows_or_columns, return_counts=True)
    if np.count_nonzero(counts == 1) == len(strings_arr_in_rows_or_columns):
        return True
    else:
        return False


# check all created strings in rows and columns, are unique or not
def are_unique_strings_in_board(node):
    board = node.board
    created_string_in_rows, created_string_in_columns = [], []

    # take out all created strings in rows
    for row in board:
        if np.count_nonzero(row == "-") == 0:
            created_string = created_string_with_char(row)
            created_string_in_rows.append(created_string)

    # take out all created strings in columns
    for i in range(len(board)):
        column = board[:, i]
        if np.count_nonzero(column == "-") == 0:
            created_string = created_string_with_char(column)
            created_string_in_columns.append(created_string)

    # check strings are in each rows and columns is unique
    if check_unique_strings(created_string_in_rows) and check_unique_strings(created_string_in_columns):
        return True
    else:
        return False
