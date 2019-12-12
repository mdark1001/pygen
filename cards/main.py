"""
@author miguelCabrera1001 | 
@date 11/12/19
@project 
@name main
"""
import datetime

from genetic import _mutar
from genetic import genetic
from .functions import mostrar, obtener_aptitud, mutacion_cards
from .aptitud import Aptitud
import unittest


class Cartas(unittest.TestCase):
    def test(self):
        size = 10
        genSet = self.initGenSet(size)
        horainico = datetime.datetime.now()

        def fnMostar(candidato):
            mostrar(candidato, horainico)

        def fnMutar(genes):
            mutacion_cards(genes, genSet)

        optimo = Aptitud(36, 360, 0)

        mejor = genetic.getBestChromosome(
            fitness=obtener_aptitud,
            sizeTarget=size,
            fitnessTarget=optimo,
            genSet=genSet,
            fnMostar=fnMostar,
            mutacionPersonalizada=fnMutar
        )
        self.assertTrue(not optimo > mejor.Fitness)

    def initGenSet(self, size):
        return [i + 1 for i in range(size)]


if __name__ == '__main__':
    unittest.main()
