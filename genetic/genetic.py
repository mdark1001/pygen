"""
@author miguelCabrera1001 | 
@date 2/10/19
@project 
@name genetic
"""
import datetime
import random
import statistics
import sys
import time
from .chromosome import Chromosome
from .functions import _generate_parent, _mutacion_personalizada, _mutar


def getBestChromosome(fitness,
                      sizeTarget,
                      fitnessTarget,
                      genSet,
                      fnMostar,
                      mutacionPersonalizada=None,
                      cromosomaPersonalizado=None):
    """
    :param fitness:
    :param sizeTarget:
    :param fitnessTarget:
    :param genSet:
    :param fnMostar:
    :param mutacionPersonalizada:
    :param cromosomaPersonalizado:
    :return:
    """
    random.seed()

    def fnMutar(parent):
        if mutacionPersonalizada is None:
            return _mutar(parent, genSet, fitness)
        return _mutacion_personalizada(parent, mutacionPersonalizada, fitness)

    def fnGenerarPadre():
        if cromosomaPersonalizado is None:
            return _generate_parent(sizeTarget, genSet, fitness)
        else:
            genes = cromosomaPersonalizado()
            return Chromosome(genes, fitness(genes))

    for mejor in getBetters(fnMutar, fnGenerarPadre):
        fnMostar(mejor)
        if not fitnessTarget > mejor.Fitness:
            return mejor


def getBetters(fnMutar, fnGenerarParent):
    bestParent = fnGenerarParent()
    yield bestParent
    while True:
        children = fnMutar(bestParent)
        if bestParent.Fitness > children.Fitness:
            continue
        if children.Fitness > bestParent.Fitness:
            bestParent = children
            continue
        yield children
        bestParent = children
