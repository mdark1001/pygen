"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name main
"""
import datetime
import unittest
from .functions import mostrar, get_attacks, obtener_aptitud, mutate, create
import random
import genetic
from .posicion import Posicion


class PruebasDeCaballos(unittest.TestCase):
    def test_3x4(self):
        anchura = 4
        altura = 4
        # 1,0   2,0   3,0
        # 0,2   1,2   2,2
        # 2 	 C C C .
        # 1 	 . . . .
        # 0 	 . C C C
        #   	 0 1 2 3
        self.main(anchura, altura, 6)

    def test_8x8(self):
        anchura = 8
        altura = 8
        self.main(anchura, altura, 14)

    def test_10x10(self):
        anchura = 10
        altura = 10
        self.main(anchura, altura, 22)

    def test_12x12(self):
        anchura = 12
        altura = 12
        self.main(anchura, altura, 28)

    # def test_13x13(self):
    #     anchura = 13
    #     altura = 13
    #     self.main(anchura, altura, 32)

    def main(self, width, height, size):
        horaInicio = datetime.datetime.now()
        todasPosiciones = [Posicion(x, y)
                           for y in range(width)
                           for x in range(height)
                           ]
        if width < 6 or height < 6:
            noBordes = todasPosiciones
        else:
            noBordes = [i for i in todasPosiciones if 0 < i.X < width - 1 and 0 < i.Y < height - 1]

        def fnMostrar(candidato):
            mostrar(candidato, horaInicio, width, height)

        def fnObtenerAptitud(genes):
            return obtener_aptitud(genes, width, height)

        def fnPositionRandon():
            # return Posicion(random.randrange(0, width), random.randrange(0, height))
            return random.choice(noBordes)

        def fnMutar(genes):
            mutate(genes, fnPositionRandon)

        def fnCrear():
            return create(fnPositionRandon, size)

        optima = width * height
        mejor = genetic.getBestChromosome(
            fitness=fnObtenerAptitud,
            sizeTarget=None,
            fitnessTarget=optima,
            genSet=None,
            fnMostar=fnMostrar,
            mutacionPersonalizada=fnMutar,
            cromosomaPersonalizado=fnCrear,

        )
        self.assertTrue(not optima > mejor.getFitness())


if __name__ == '__main__':
    unittest.main()
