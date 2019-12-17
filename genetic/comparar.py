"""
@author miguelCabrera1001 | 
@date 16/12/19
@project 
@name comparar
"""

import statistics
import sys

import time


class Comparar:
    @staticmethod
    def ejecutar(funcion):
        print(funcion)
        cronometrajes = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            horaInicio = time.time()
            funcion()
            segundos = time.time() - horaInicio
            sys.stdout = stdout
            cronometrajes.append(segundos)
            promedio = statistics.mean(cronometrajes)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, promedio,
                    statistics.stdev(cronometrajes,
                                     promedio) if i > 1 else 0))
