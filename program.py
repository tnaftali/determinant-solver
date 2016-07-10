from Classes import Pivot
from Validation import is_number, is_valid_range


def insert_matrix():
    str_range = raw_input('Please insert the range of a square matrix: ')
    is_valid_range(str_range)
    while not is_valid_range(str_range):
        str_range = raw_input('Please insert a valid positive number, higher than 1: ')
    mat_range = int(str_range)
    matrix = []
    for i in range(mat_range):
        string_row = raw_input('Insert row ' + str(i + 1) + ', with ' + str(mat_range) + ' numbers separated by comma: ')
        int_row = get_row(string_row, mat_range)
        while int_row is None:
            string_row = raw_input('Insert row ' + str(i + 1) + ', with ' + str(mat_range) +
                                   ' valid numbers separated by comma: ')
            int_row = get_row(string_row, mat_range)
        matrix.append(int_row)
    return matrix


def get_row(row, range):
    numbers = row.replace(' ', '').split(',')
    length = len(numbers)
    int_row = []
    valid = True
    i = 0
    if length == range:
        while i < length and valid:
            num = numbers[i]
            if is_number(num):
                int_row.append(int(num))
            else:
                valid = False
            i += 1
        if valid:
            return int_row
        else:
            return None
    else:
        return None


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
        length = len(matrix)
        if length > 2:
            pivot = Pivot(matrix)
            reduced_matrix = get_reduced_matrix(matrix, pivot)
            return pivot.number * pow(-1, ((pivot.row_index + 1) + (pivot.col_index + 1))) * calculate_determinant(reduced_matrix)
        else:
            return calculate(matrix)


def get_reduced_matrix(matrix, pivot):
    mat_range = len(matrix)
    if mat_range == 2:
        res = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        return res
    else:
        operating_row = matrix[pivot.row_index]
        new_matrix = []
        # Up rows
        if pivot.row_index != 0:
            for i in range(pivot.row_index - 1, -1, - 1):
                new_matrix.insert(0, operate_rows(matrix[i], operating_row, pivot.col_index))
        if pivot.row_index != (mat_range - 1):
            # Down rows
            for i in range(pivot.row_index + 1, mat_range):
                new_matrix.append(operate_rows(matrix[i], operating_row, pivot.col_index))
        return remove_pivot_column(new_matrix, pivot.col_index)


def calculate(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def operate_rows(row1, row2, col_index):
    length = len(row1)
    result = []
    minus = False
    if row1[col_index] > 0:
        minus = True
    for i in range(length):
        if minus:
            result.append(row1[i] - (row1[col_index] * row2[i]))
        else:
            result.append(row1[i] + (row1[col_index] * row2[i]))
    return result


def remove_pivot_column(matrix, col_index):
    length = len(matrix)
    for i in range(length):
        del matrix[i][col_index]
    return matrix


def print_matrix(matrix):
    print "------------"
    for i in range(len(matrix)):
        print matrix[i]
    print "------------"


def main():
    print '-------------------------------------------------------'
    matrix = insert_matrix()
    print "Matrix: "
    print_matrix(matrix)
    print 'Determinant: ' + str(calculate_determinant(matrix))

main()
print 'Another one?'
repeat = raw_input('\'Y\' \'N\':')
while repeat.lower() == 'y':
    main()
    print 'Another one?'
    repeat = raw_input('\'Y\' \'N\':')
