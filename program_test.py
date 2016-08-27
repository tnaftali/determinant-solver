import unittest
import program


class ProgramTest(unittest.TestCase):

    def test_notEmptyRange2Matrix(self):
        self.assertEqual(program.mode_2('1,0;0,1'), 1)

    def test_emptyRange2Matrix(self):
        self.assertEqual(program.mode_2('0,0;0,0'), 0)

    def test_notEmptyRange3Matrix(self):
        self.assertEqual(program.mode_2('5,3,7;2,4,9;3,6,4'), -133.0)

    def test_emptyRange3Matrix(self):
        self.assertEqual(program.mode_2('0,0,0;0,0,0;0,0,0'), 0)

    def test_range3MatrixWithNegatives(self):
        self.assertEqual(program.mode_2('-5,3,7;2,-4,9;-3,6,-7'), 91)

    def test_range4MatrixWithNegativesAndZeros(self):
        string_matrix = '-5,3,7,0;2,-4,9,-3;-3,6,-7,6;5,6,-2,-8'
        self.assertEqual(program.mode_2(string_matrix), -2507)

    def test_range4MatrixWithNegativesAndZerosStartingWithZero(self):
        string_matrix = '0,3,7,0;2,-4,9,-3;-3,6,-7,6;5,6,-2,-8'
        self.assertEqual(program.mode_2(string_matrix), -537)
