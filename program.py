import Determinant
import Input


def print_matrix(matrix):
    print "------------"
    for i in range(len(matrix)):
        print matrix[i]
    print "------------"


def mode_1():
    print '-------------------------------------------------------'
    matrix = Input.insert_matrix()
    print "Matrix: "
    print_matrix(matrix)
    print 'Determinant: ' + str(Determinant.calculate_determinant(matrix))


def mode_2(string_matrix):
    matrix = Input.get_matrix(string_matrix)
    result = Determinant.calculate_determinant(matrix)
    return int(str(result).split('.')[0])


def main():
    mode_1()
    print 'Another one?'
    repeat = raw_input('\'Y\' \'N\':')
    while repeat.lower() == 'y':
        mode_1()
        print 'Another one?'
        repeat = raw_input('\'Y\' \'N\':')

# main()