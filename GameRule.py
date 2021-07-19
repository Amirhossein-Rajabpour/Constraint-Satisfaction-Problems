import copy

import numpy as np
from Main import *
from Node import *


# calculate number of digit in row or column
def calculate_number_of_digit(row_or_column, digit):
    # count_digit = np.count_nonzero(row_or_column == digit)
    count_digit = row_or_column.count(digit)
    return count_digit


# check numbers of digit in each row and column (first rule)
def is_equal_numbers_of_digit_in_board(node):
    board = node.board

    # check rows
    for row in board:
        if row.count('-') == 0:
            if row.count("0") != row.count("1"):
                return False

    # check columns
    for i in range(len(board)):
        column = board[:][i]
        if column.count('-') == 0:
            if column.count("0") != column.count("1"):
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


# check all created strings in rows and columns, are unique or not  (second rule)
def are_unique_strings_in_board(node):
    board = node.board
    created_string_in_rows, created_string_in_columns = [], []

    # take out all created strings in rows
    for row in board:
        if row.count('-') == 0:
            created_string = created_string_with_char(row)
            created_string_in_rows.append(created_string)

    # take out all created strings in columns
    for i in range(len(board)):
        column = board[:][i]
        if column.count('-') == 0:
            created_string = created_string_with_char(column)
            created_string_in_columns.append(created_string)

    # check strings are in each rows and columns is unique
    if check_unique_strings(created_string_in_rows) and check_unique_strings(created_string_in_columns):
        return True
    else:
        return False


# check duplicate digit in row or column
def check_duplicate_digit(row_or_column):
    if len(row_or_column) >= 3:
        for i in range(0, len(row_or_column) - 2):
            if row_or_column[i] == row_or_column[i + 1] == row_or_column[i + 2] and row_or_column[i] != "-":
                return False

    return True


# check duplicate digit in rows and columns in board
def check_duplicate_digit_in_board(node):
    board = node.board

    # check rows
    for row in board:
        if not check_duplicate_digit(row):
            return False

    # check columns
    for i in range(len(board)):
        column = board[:][i]
        if not check_duplicate_digit(column):
            return False

    return True


def check_all_rule_game(node):
    if is_equal_numbers_of_digit_in_board(node) and are_unique_strings_in_board(
            node) and check_duplicate_digit_in_board(node):
        return True
    else:
        return False


def count_object_in_array(arr, object):
    counter = 0
    for i in range(len(arr)):
        if arr[i] == object:
            counter += 1

    return counter


def chek_new_domain_length(new_domain):
    pass


def check_variables_domain_with_rule1(variables_domain, variable_index):
    x, y = variable_index[0], variable_index[1]

    row = variables_domain[x][:]
    column = variables_domain[:][y]
    new_domain = variables_domain[x][y]

    # check row
    if row.count("0") + count_object_in_array(row, ["0"]) >= len(row) / 2 and "0" in new_domain:
        # np.delete(new_domain, np.where(new_domain == "0"))
        new_domain.remove("0")
    if row.count("1") + count_object_in_array(row, ["1"]) >= len(row) / 2 and "1" in new_domain:
        # np.delete(new_domain, np.where(new_domain == "1"))
        new_domain.remove("1")

    # check column
    if row.count("0") + count_object_in_array(column, ["0"]) >= len(column) / 2 and "0" in new_domain:
        # np.delete(new_domain, np.where(new_domain == "0"))
        new_domain.remove("0")
    if row.count("1") + count_object_in_array(column, ["1"]) >= len(column) / 2 and "1" in new_domain:
        # np.delete(new_domain, np.where(new_domain == "1"))
        new_domain.remove("1")

    return new_domain


# get variable_index and check duplicate digit rule
def check_variables_domain_duplicate_digit(row_or_column, variable_index, domain):
    new_domain = domain
    k = variable_index

    if k >= 2 and row_or_column[k - 1] == row_or_column[k - 2] and (
            row_or_column[k - 1] == "0" or row_or_column[k - 1] == "1") and row_or_column[k - 1] in new_domain:
        new_domain.remove(row_or_column[k - 1])
        # np.delete(new_domain, np.where(new_domain == row_or_column[k - 1]))
    if k <= len(row_or_column) - 3 and row_or_column[k + 1] == row_or_column[k + 2] and (
            row_or_column[k + 1] == "0" or row_or_column[k + 1] == "1") and row_or_column[k + 1] in new_domain:
        new_domain.remove(row_or_column[k + 1])
        # np.delete(new_domain, np.where(new_domain == row_or_column[k - 1]))

    return new_domain


def check_variables_domain_with_rule3(variables_domain, variable_index):
    x, y = variable_index[0], variable_index[1]
    domain = variables_domain[x][y]

    # check in row
    row = variables_domain[x][:]
    new_domain = check_variables_domain_duplicate_digit(row, y, domain)

    # check in column
    column = variables_domain[:][y]
    new_domain = check_variables_domain_duplicate_digit(column, x, new_domain)

    return new_domain


def check_variables_domains_with_rule_game(variables_domain, variable_index):
    variables_domain_copy = copy.deepcopy(variables_domain)
    x, y = variable_index[0], variable_index[1]

    # check rule 1
    new_domain = check_variables_domain_with_rule1(variables_domain_copy, variable_index)
    if len(new_domain) == 0:
        return False, []
    variables_domain_copy[x][y] = new_domain

    # check rule 3
    new_domain = check_variables_domain_with_rule3(variables_domain_copy, variable_index)
    if len(new_domain) == 0:
        return False, []
    variables_domain_copy[x][y] = new_domain

    return True, variables_domain_copy


if __name__ == "__main__":
    board = np.array([["1", "1", "0", "0"],
                      ["0", "1", "1", "0"],
                      ["1", "0", "0", "1"],
                      ["0", "0", "1", "1"]])
    node = Node(board, "", "")
    print(check_all_rule_game(node))
