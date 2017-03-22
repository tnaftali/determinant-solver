import Validation


def insert_matrix():
    str_range = input('Please insert the range of a square matrix: ')
    Validation.is_valid_range(str_range)
    while not Validation.is_valid_range(str_range):
        str_range = input('Please insert a valid positive number, higher than 1: ')
    mat_range = int(str_range)
    matrix = []
    for i in range(mat_range):
        string_row = input('Insert row ' + str(i + 1) + ', with ' + str(mat_range) + ' numbers separated by comma: ')
        float_row = get_row(string_row, mat_range)
        while float_row is None:
            string_row = input('Insert row ' + str(i + 1) + ', with ' + str(mat_range) +
                               ' valid numbers separated by comma: ')
            float_row = get_row(string_row, mat_range)
        matrix.append(float_row)
    return matrix


def get_row(row, range):
    numbers = row.replace(' ', '').split(',')
    length = len(numbers)
    float_row = []
    valid = True
    i = 0
    if length == range:
        while i < length and valid:
            num = numbers[i]
            float_num = Validation.is_number(num)
            if float_num is not None:
                float_row.append(float_num)
            else:
                valid = False
            i += 1
        if valid:
            return float_row
        else:
            return None
    else:
        return None


def get_matrix(string_matrix):
    matrix = []
    rows = string_matrix.split(';')
    for i in range(len(rows)):
        row = []
        num = rows[i].split(',')
        for j in range(len(num)):
            row.append(float(num[j]))
        matrix.append(row)
    return matrix
