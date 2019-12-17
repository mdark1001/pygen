"""
@author miguelCabrera1001 | 
@date 16/12/19
@project 
@name Chromosome
"""


class Chromosome(object):
    def __init__(self, genes, fitness):
        self.Gen = genes
        self.Fitness = fitness

    def getGenesStr(self):
        return list(map(str, self.Gen))

    def getGenes(self):
        return list(self.Gen)

    def getFitness(self):
        return self.Fitness
