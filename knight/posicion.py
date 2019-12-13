"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name posicion
"""


class Posicion:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "({} , {})".format(self.X, self.Y)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __hash__(self):
        return self.X * 1000 + self.Y
