"""
@author miguelCabrera1001 | 
@date 11/12/19
@project 
@name functions
"""
import datetime
import functools
import operator
import random

from .aptitud import Aptitud


def getlistParcial(lista, inicio, fin):
    return ','.join(map(str, lista[inicio:fin]))


def mutacion_cards(genes, genSet):
    if len(genes) == len(set(genSet)):
        indiceA, indiceB = random.sample(range(len(genes)), 2)
        genes[indiceA], genes[indiceB] = genes[indiceB], genes[indiceA]
    else:
        indiceA = random.randrange(0, len(genes))
        indiceB = random.randrange(0, len(genSet))
        genes[indiceA] = genes[indiceB]


def obtener_aptitud(genes):
    suma_grupo1 = sum(genes[0:5])
    producto_grupo2 = functools.reduce(operator.mul, genes[5:10])
    duplicados = (len(genes) - len(set(genes)))
    return Aptitud(suma_grupo1, producto_grupo2, duplicados)


def mostrar(candidato, horaInicio):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print(" {} - {}\t{}\t{} ".format(
        getlistParcial(candidato.getGenes(), 0, 5),
        getlistParcial(candidato.getGenes(), 5, 10),
        candidato.Fitness,
        diferencia
    ))
