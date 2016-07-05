import random


class Pivot(object):
    number = None

    def __init__(self, max):
        max -= 1
        self.row_index = self.get_random_number(max)
        self.col_index = self.get_random_number(max)
        while self.col_index == self.row_index:
            self.col_index = self.get_random_number(max)

    @staticmethod
    def get_random_number(max):
        return random.randint(0, max)
