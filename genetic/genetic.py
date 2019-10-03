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


def _generate_parent(size, genSet, fitness):
    """
    :param size:
    :param genSet:
    :param fitness:
    :return:
    """
    genes = []
    while len(genes) < size:
        sizeMuestral = min(size - len(genes), len(genSet))
        genes.extend(random.sample(genSet, sizeMuestral))
    genes = genes
    fit = fitness(genes)
    return Chromosome(genes, fit)


def _mutar(parent, genSet, fitness):
    """
    :param parent:
    :param genSet:
    :param fitness:
    :return:
    """
    index = random.randrange(0, len(parent.Gen))
    genChildren = list(parent.Gen)
    newGen, pivot = random.sample(genSet, 2)
    genChildren[index] = pivot if newGen == genChildren[index] else newGen
    genes = genChildren
    fit = fitness(genes)
    return Chromosome(genes, fit)


def getBestChromosome(fitness, sizeTarget, fitnessTarget, genSet, show):
    random.seed()
    bestParent = _generate_parent(size=sizeTarget,
                                  genSet=genSet,
                                  fitness=fitness)
    show(bestParent)
    if bestParent.Fitness >= fitnessTarget:
        return bestParent
    while True:
        children = _mutar(parent=bestParent, genSet=genSet, fitness=fitness)
        if bestParent.Fitness >= children.Fitness:
            continue
        show(children)
        if children.Fitness >= fitnessTarget:
            return children
        bestParent = children


def mostrar(candidato, horaInicio):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print("{}\t{}\t{}".format(
        ' '.join(candidato.getGenes()), candidato.Fitness, diferencia)
    )


class Chromosome(object):
    def __init__(self, genes, fitness):
        self.Gen = genes
        self.Fitness = fitness

    def getGenes(self):
        return list(map(str, self.Gen))


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


1
