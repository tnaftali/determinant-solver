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
    def get_inverse(num):
        return 1 / num