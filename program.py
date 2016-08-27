import Determinant
import Input
import Output


def mode_1():
    print '-------------------------------------------------------'
    matrix = Input.insert_matrix()
    print "Matrix: "
    Output.print_matrix(matrix)
    print 'Determinant: ' + str(Determinant.calculate_determinant(matrix))


def mode_2(string_matrix):
    matrix = Input.get_matrix(string_matrix)
    result = Determinant.calculate_determinant(matrix)
    if result != 0:
        return Output.round_number(result)
    else:
        return 0


def main():
    mode_1()
    print 'Another one?'
    repeat = raw_input('\'Y\' \'N\':')
    while repeat.lower() == 'y':
        mode_1()
        print 'Another one?'
        repeat = raw_input('\'Y\' \'N\':')


# Uncomment this to execute program
# main()
