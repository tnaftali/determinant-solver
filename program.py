# Algorithm that solves the determinant of any square range matrix.
# Created by Tobias Naftali https://github.com/tnaftali/

import Determinant
import Input
import Output


def manual_input():
    print('-------------------------------------------------------')
    matrix = Input.insert_matrix()
    print("Matrix: ")
    Output.print_matrix(matrix)
    result = Determinant.calculate_determinant(matrix)
    print('Determinant: ' + str(Output.round_number(result)))


def parameter_input(string_matrix):
    matrix = Input.get_matrix(string_matrix)
    result = Determinant.calculate_determinant(matrix)
    if str(result).lower().__contains__('e'):
        return Output.exponential_output(result)
    else:
        if result != 0:
            return Output.round_number(result)
        else:
            return 0


def main():
    manual_input()
    print('Another one?')
    repeat = input('\'Y\' \'N\':')
    while repeat.lower() == 'y':
        manual_input()
        print('Another one?')
        repeat = input('\'Y\' \'N\':')


# Uncomment this to execute program, comment to run tests
main()
