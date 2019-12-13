"""
@author miguelCabrera1001 | 
@date 6/12/19
@project 
@name main
"""
import datetime

from  genetic import genetic
from .functions import getFitnessByGenes,printBoard
from .aptitud import Fitness
import unittest


class TestQueens(unittest.TestCase):
    def main(self, size=8):
        """
        :param size:
        :return: False
        """
        genSet = self.generateGeneticSet(size)  # Inicializar el conjunto de Genes
        print(genSet)
        startTime = datetime.datetime.now()

        def fnDisplay(candidato):
            printBoard(candidato, startTime, size)

        def fnGetFitness(genes):
            return getFitnessByGenes(genes, size)

        optimo = Fitness(0)
        bestBoard = genetic.getBestChromosome(fitness=fnGetFitness,
                                              sizeTarget=2 * size,
                                              fitnessTarget=optimo,
                                              genSet=genSet,
                                              fnMostar=fnDisplay
                                              )
        self.assertTrue(not optimo > bestBoard.Fitness)

    def test_8(self):
        self.main(size=8)

    def test_16(self):
        self.main(size=16)

    def test_32(self):
        self.main(32)

    def generateGeneticSet(self, size):
        return [i for i in range(size)]


if __name__ == '__main__':
    unittest.main()
