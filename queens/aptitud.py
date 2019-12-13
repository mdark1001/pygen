"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name aptitud
"""


class Fitness(object):
    def __init__(self, total):
        self.total = total

    def __gt__(self, other):
        return self.total < other.total

    def __str__(self):
        return "{}".format(self.total)
