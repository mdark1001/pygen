"""
@author miguelCabrera1001 | 
@date 2/10/19
@project 
@name password.py
"""
import datetime
import random
import unittest

import genetic


def obtener_aptitud(conjetura, objetivo):
    return sum(1 for esperado, real in zip(objetivo, conjetura)
               if esperado == real)


def mostrar(candidato, horaInicio):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print("{}\t{}\t{}".format(
        candidato.Gen, candidato.Fitness, diferencia))


class TestPassword(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!¡.,"

    def test_Hola_Mundo(self):
        objetivo = "¡Hola Mundo!"
        self.findPassword(objetivo)

    def findPassword(self, objetivo):
        horaInicio = datetime.datetime.now()

        def fnObtenerAptitud(genes):
            return obtener_aptitud(genes, objetivo)

        def fnMostrar(candidato):
            mostrar(candidato, horaInicio)

        aptitudOptima = len(objetivo)
        mejor = genetic.getBestChromosome(fnObtenerAptitud,
                                          len(objetivo),
                                          aptitudOptima, self.geneSet,
                                          fnMostrar)
        self.assertEqual(mejor.Gen, objetivo)

    def test_lorem(self):
        frase = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno"
        self.findPassword(frase)


if __name__ == '__main__':
    unittest.main()
