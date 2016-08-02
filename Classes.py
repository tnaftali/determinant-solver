import decimal

class Pivot(object):
    def __init__(self, matrix):
        self.row_index = 0
        self.col_index = 0
        self.number = matrix[self.row_index][self.col_index]
        inverse_of_first = self.get_inverse(matrix[0][0])
        for i in range(len(matrix)):
            dec = decimal.Decimal(matrix[0][i]) * decimal.Decimal(inverse_of_first)
            matrix[0][i] = format(dec, '.10f')
        self.new_matrix = matrix
    @staticmethod
    def search_for_1_in_matrix(matrix):
        result = []
        exists = False
        length = len(matrix)
        i = 0
        while i < length and not exists:
            j = 0
            while j < length and not exists:
                if matrix[i][j] == 1:
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