import unittest
import program
import Output


class ProgramTest(unittest.TestCase):

    def test_notEmptyRange2Matrix(self):
        self.assertEqual(program.parameter_input('1,0;0,1'), 1)

    def test_emptyRange2Matrix(self):
        self.assertEqual(program.parameter_input('0,0;0,0'), 0)

    def test_notEmptyRange3Matrix(self):
        self.assertEqual(program.parameter_input('5,3,7;2,4,9;3,6,4'), -133.0)

    def test_emptyRange3Matrix(self):
        self.assertEqual(program.parameter_input('0,0,0;0,0,0;0,0,0'), 0)

    def test_range3MatrixWithNegatives(self):
        self.assertEqual(program.parameter_input('-5,3,7;2,-4,9;-3,6,-7'), 91)

    def test_range4MatrixWithNegativesAndZeros(self):
        string_matrix = '-5,3,7,0;2,-4,9,-3;-3,6,-7,6;5,6,-2,-8'
        self.assertEqual(program.parameter_input(string_matrix), -2507)

    def test_range4MatrixWithNegativesAndZerosStartingWithZero(self):
        string_matrix = '0,3,7,0;2,-4,9,-3;-3,6,-7,6;5,6,-2,-8'
        self.assertEqual(program.parameter_input(string_matrix), -537)

    def test_range5MatrixWithNegatives(self):
        string_matrix = '22,39,14,91,57;-53,-99,71,27,-23;-47,32,-41,-62,-58;26,-12,11,-33,31;-35,-63,-13,25,-90'
        self.assertEqual(program.parameter_input(string_matrix), 212085522)

    def test_range5MatrixWithNegativesAndZerosStartingWithZero(self):
        string_matrix = '0,0,14,91,57;-53,-99,71,27,-23;0,32,-41,-62,-58;26,0,11,-33,31;-35,-63,-13,25,-90'
        self.assertEqual(program.parameter_input(string_matrix), 13729398)
        
    def test_range6MatrixWithNegatives(self):
        string_matrix = '8508,-9325,-9362,-2614,-7723,336;-7099,-7193,8985,-212,1975,-2149;-1740,9829,-8170,2691,' \
                        '-6467,-3067;-2354,-2589,4993,9189,-6668,9802;8512,-4038,902,8556,-8036,6985;-2253,' \
                        '5926,-7050,4402,844,-5675'
        result = 1300658708375767858497913
        self.assertEqual(program.parameter_input(string_matrix), Output.exponential_output(result))

    def test_range7MatrixWithNegativesAndZerosStartingWithZero(self):
        string_matrix = '28,100,85,-26,45,-5,7;-14,-91,-7,-76,-71,-56,41;37,1,17,90,64,-33,82;93,72,38,43,-38,73,-54;' \
                        '-28,47,66,-9,48,-30,59;-23,-13,29,-20,-17,21,-3;-64,-99,3,84,49,5,-81'
        result = -25676744657955
        self.assertEqual(program.parameter_input(string_matrix), result)

    def test_range10MatrixWithNegatives(self):
        string_matrix = '28,45,-73,-75,46,36,21,26,48,30;-86,38,-32,82,-22,-19,-29,100,-72,-3;13,84,-76,-99,-78,94,14' \
                        ',-12,-4,56;43,-91,1,97,-11,59,61,-16,-31,-43;-60,-63,41,-52,-95,86,67,88,79,8;-28,-62,-20,' \
                        '-34,-51,12,-5,35,-8,-55;15,-93,34,-14,-54,-17,98,-85,-24,72;-81,18,-30,-47,50,11,39,66,90,7;' \
                        '-98,-87,-84,20,-97,89,19,-13,60,-23;96,44,-71,-36,-46,25,32,85,54,77'
        result = 619266553777932419372
        self.assertEqual(program.parameter_input(string_matrix), Output.exponential_output(result))

    def test_range12MatrixWithNegatives(self):
        string_matrix = '-2,9,-46,17,50,-73,8,76,29,-77,-69,15;69,-16,65,62,24,-6,71,-80,40,-84,-19,95;27,-33,' \
                        '-75,-23,-67,-25,-27,36,89,70,-47,-29;85,-90,-97,84,-82,-39,-65,-26,-96,7,100,14;-49,' \
                        '-9,81,13,38,82,0,-66,-14,44,48,94;-42,78,-35,-86,54,-4,-59,66,4,-72,21,-52;55,39,-58,' \
                        '-57,-53,-85,-20,-18,49,-79,72,92;83,97,74,52,43,-36,-76,-24,-54,22,56,23;-37,93,-32,18,' \
                        '-10,-78,3,28,-15,96,-41,-31;-81,47,75,33,12,-94,98,-64,-38,19,-70,-21;80,-48,-7,11,25,' \
                        '42,31,-56,32,-51,91,-87;-91,63,10,-99,-93,58,26,-45,20,-92,-55,88'
        result = 3708810380587217049754426
        self.assertEqual(program.parameter_input(string_matrix), Output.exponential_output(result))
