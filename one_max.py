"""
@author miguelCabrera1001 | 
@date 2/10/19
@project 
@name one_max
"""
import datetime
import unittest
import genetic


def obtener_aptitud(conjetura,objetivo):
    return conjetura.count(1)





class TestOneMax(unittest.TestCase):
    geneSet = [0,1]

    def test_buscar_10(self):
        self.findOneMax(10)

    def test_buscar_50(self):
        self.findOneMax(50)

    def test_buscar_100(self):
        self.findOneMax(100)

    def findOneMax(self, objetivo):
        horaInicio = datetime.datetime.now()

        def fnObtenerAptitud(genes):
            return obtener_aptitud(genes, objetivo)

        def fnMostrar(candidato):
            genetic.mostrar(candidato, horaInicio)

        aptitudOptima = objetivo
        mejor = genetic.getBestChromosome(fnObtenerAptitud,
                                            objetivo,
                                            aptitudOptima, self.geneSet,
                                            fnMostrar)
        self.assertEqual(mejor.Fitness, objetivo)


if __name__ == '__main__':
    unittest.main()
