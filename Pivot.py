import decimal


class Pivot(object):
    def __init__(self, matrix):
        self.none = False
        indexes = self.not_null_indexes(matrix)
        if indexes is not None:
            self.row_index = indexes[0]
            self.col_index = indexes[1]
            self.number = matrix[self.row_index][self.col_index]
            inverse_of_first = self.get_inverse(self.number)
            for i in range(len(matrix)):
                dec = decimal.Decimal(matrix[self.row_index][i]) * decimal.Decimal(inverse_of_first)
                matrix[self.row_index][i] = format(dec, '.1000')
            self.new_matrix = matrix
        else:
            self.none = True

    @staticmethod
    def not_null_indexes(matrix):
        result = []
        exists = False
        length = len(matrix)
        i = 0
        while i < length and not exists:
            j = 0
            while j < length and not exists:
                if matrix[i][j] != 0:
                    result.append(i)
                    result.append(j)
                    exists = True
                j += 1
            i += 1
        if exists:
            return result
        else:
            return None

    @staticmethod
    def get_inverse(num):
        return 1 / num
