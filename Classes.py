class Pivot(object):
    def __init__(self, matrix):
        indexes = self.search_for_1_in_matrix(matrix)
        if indexes is not None:
            self.row_index = indexes[0]
            self.col_index = indexes[1]
            self.number = matrix[self.row_index][self.col_index]

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
