from Classes import Pivot
import math


def insert_matrix():
    matrix = []
    str_range = raw_input("Please insert the range of a squared matrix: ")
    is_valid_range(str_range)
    while not is_valid_range(str_range):
        str_range = raw_input("Please insert a valid positive number: ")
    mat_range = int(str_range)
    for i in range(mat_range):
        matrix.append([])
        for j in range(mat_range):
            num_str = raw_input("Row " + str(i + 1) + ", Col " + str(j + 1) + ": ")
            while not is_number(num_str):
                num_str = raw_input("Please insert valid number for Row " + str(i + 1) + ", Col " + str(j + 1) + ": ")
            num = int(num_str)
            matrix[i].append(num)
    # matrix = []
    # string_matrix = raw_input('Please insert a numeric matrix, with numbers in same row separated by comma,'
    #                           'and rows separated by semicolon: ')
    # str_rows = string_matrix.split(';')
    # for row in str_rows:
    #     validate_row(row)
    # while not valid_string_matrix(str_rows):
    #     string_matrix = raw_input('Please insert all valid numbers, separated by comma in same row,'
    #                               'and rows separated by semicolon: ')
    #     str_rows = string_matrix.replace(' ', '').split(';')
    # # matrix = parse_string_matrix(str_matrix)
    # # print_matrix(str_matrix)
    return matrix


def valid_string_matrix(str_matrix):
    valid = True
    for x in str_matrix:
        if not is_number(x):
            valid = False
    if valid:
        # Check whether the matrix is square
        length = len(str_matrix)
        # if math.sqrt(length).is_integer():
        print math.sqrt(length)
    return valid


def initialize_matrix(mat_range):
    num = 1
    matrix = []
    for i in range(mat_range):
        matrix.append([])
        for j in range(mat_range):
            matrix[i].append(num)
        num += 1
    return matrix


def calculate_determinant(matrix):
    if not isinstance(matrix, list):
        return matrix
    else:
        pivot = Pivot(len(matrix))
        pivot.number = matrix[pivot.row_index][pivot.col_index]
        while pivot.number == 0:
            pivot = Pivot(len(matrix))
        get_reduced_matrix(matrix, pivot)
        # det = calculate_determinant(reduced_matrix)
        # res = pivot * det
        # return res
        return 1


def get_reduced_matrix(matrix, pivot):
    mat_range = len(matrix)
    if mat_range == 2:
        res = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        return res
    else:
        pivot_row = [matrix[pivot.row_index]]
        # Up rows
        print pivot.row_index
        for i in range(pivot.row_index, 0, - 1):
            print i
            make_0(matrix[i], matrix[i - 1], pivot.col_index)
        # Down rows
        for i in range(pivot.row_index + 1, mat_range):
            if i != mat_range - 1:
                make_0(matrix[i], matrix[i + 1], pivot.col_index)
            else:
                make_0(matrix[i], matrix[pivot.row_index], pivot.col_index)
        # for i in range(1, mat_range):
        #     if i == (mat_range - 1):
        #         aux_matrix.append(make_0_first(matrix[i], matrix[0]))
        #     else:
        #         aux_matrix.append(make_0_first(matrix[i], matrix[i + 1]))
        # # print_matrix(aux_matrix)
        # reduced_matrix = get_new_matrix(aux_matrix, mat_range)
        # print_matrix(reduced_matrix)
        # return reduced_matrix


def get_new_matrix(det, mat_range):
    new_mat = []
    for i in range(1, mat_range):
        new_mat.append([])
        for j in range(1, mat_range):
            new_mat[i - 1].append(det[i][j])
    return new_mat


def make_0(row1, row2, col_index):
    length = len(row1)
    result = []
    print str(row2[col_index]) + str(row1) + " - " + str(row1[col_index]) + str(row2)
    for i in range(length):
        result.append((row2[0] * row1[i]) - (row1[0] * row2[i]))
    print "Result: " + str(result)
    return result


def is_valid_range(num_str):
    valid = True
    if not is_number(num_str):
        valid = False
    else:
        num = int(num_str)
        if not is_positive(num):
            valid = False
    return valid


def is_number(num):
    try:
        val = int(num)
        return True
    except ValueError:
        return False


def is_positive(num):
    if num > 0:
        return True
    else:
        return False


def print_matrix(matrix):
    print "------------"
    for i in range(len(matrix)):
        print matrix[i]
    print "------------"


mat_range = 3
matrix = initialize_matrix(mat_range)
# matrix = insert_matrix()
print "Original Matrix: "
print_matrix(matrix)

calculate_determinant(matrix)
