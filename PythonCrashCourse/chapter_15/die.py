from random import randint

class Die:
    def __init__(self, num_sides = 6):
        """A class responding to a single die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random value between one and number of sides"""
        return randint(1,self.num_sides)