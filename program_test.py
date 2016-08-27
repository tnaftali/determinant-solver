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
