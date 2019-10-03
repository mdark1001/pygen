"""
@author miguelCabrera1001 | 
@date 2/10/19
@project 
@name sort_numbers
"""
import datetime
import unittest
import genetic


def obtener_aptitud(conjetura, objetivo):
    aptitud = 1
    for i in range(1, len(conjetura)):
        if conjetura[i] > conjetura[i - 1]:
            aptitud += 1
    return aptitud


class TestSortNumbers(unittest.TestCase):
    geneSet = []

    def test_sort_10(self):
        self.sortList(10)

    def test_sort_50(self):
        self.sortList(50)

    def test_sort_100(self):
        self.sortList(100)

    def sortList(self, objetivo):
        horaInicio = datetime.datetime.now()

        def fnObtenerAptitud(genes):
            return obtener_aptitud(genes, objetivo)

        def fnMostrar(candidato):
            genetic.mostrar(candidato, horaInicio)

        aptitudOptima = 1
        self.geneSet = [i for i in range(100)]
        mejor = genetic.getBestChromosome(fnObtenerAptitud,
                                          objetivo,
                                          aptitudOptima, self.geneSet,
                                          fnMostrar)

        self.assertTrue(not aptitudOptima > mejor.Fitness)


if __name__ == '__main__':
    unittest.main()
