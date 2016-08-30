from Pivot import Pivot


def calculate_determinant(matrix):
    if not isinstance(matrix, list):  # Checks whether the matrix is an instance, if it is, it should be the result
                                        # so it returns it
        return matrix
    else:
        length = len(matrix)
        if length > 2:
            pivot = Pivot(matrix)  # Creates new Pivot object
            if pivot.none:  # If it's none, the matrix is null (all zero)
                return 0
            else:
                reduced_matrix = get_reduced_matrix(pivot.new_matrix, pivot)
                return float(pivot.number) * (
                    float(pow(-1, ((pivot.row_index + 1) + (pivot.col_index + 1)))) * calculate_determinant(reduced_matrix))
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
        if pivot.row_index != 0:  # Up rows
            for i in range(pivot.row_index - 1, -1, - 1):
                new_matrix.insert(0, operate_rows(matrix[i], operating_row, pivot.col_index))
        if pivot.row_index != (mat_range - 1):
            for i in range(pivot.row_index + 1, mat_range):  # Down rows
                new_matrix.append(operate_rows(matrix[i], operating_row, pivot.col_index))
        return remove_pivot_column(new_matrix, pivot.col_index)


def calculate(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def operate_rows(row1, row2, col_index):
    length = len(row1)
    result = []
    if row1[col_index] == 0:
        result = row1
    else:
        for i in range(length):
            res = row1[i] - (float(row1[col_index]) * float(row2[i]))
            result.append(res)
    return result


def remove_pivot_column(matrix, col_index):
    length = len(matrix)
    for i in range(length):
        del matrix[i][col_index]
    return matrix
