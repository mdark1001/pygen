"""
@author miguelCabrera1001 | 
@date 16/12/19
@project 
@name functions
"""
import datetime
import random

from .chromosome import Chromosome


def _generate_parent(size, genSet, fitness):
    """
    :param size: Tamaño de la cadena que comprende al individuo
    :param genSet: Un conjunto  de genes por ejemplo un array
    :param fitness: el nombre de una función pasada para calcular el fitness (Aptitud del nuevo individuo)
    :return:Object  Chromosome() contiene la definición  de un individuo
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
    Realizar las modificaciones en el código genetico de un individuo

    :param parent: Un Chromosome Objecto ()
    :param genSet: Conjuto de carácteristicas un  Array
    :param fitness: Función para calcular la aptitud de un individuo
    :return: Object  Chromosome() contiene la definición  de un individuo
    """
    index = random.randrange(0, len(parent.Gen))
    genChildren = parent.getGenes()
    newGen, pivot = random.sample(genSet, 2)
    genChildren[index] = pivot if newGen == genChildren[index] else newGen
    genes = genChildren
    fit = fitness(genes)
    return Chromosome(genes, fit)


def _mutacion_personalizada(parent, _mutacion, fitness):
    """
    :param parent:  : Un Chromosome Objecto ()
    :param _mutacion: Nonbre de una función para realizar modificaciones en el código genetico de un individuo
    :param fitness: Función para calcular la aptitud de un individuo
    :return: : Un Chromosome Objecto ()
    """
    genChildren = parent.getGenes()
    _mutacion(genChildren)
    fit = fitness(genChildren)
    return Chromosome(genChildren, fit)


def mostrar(candidato, horaInicio):
    """
    Inprimir la lista de genes de un individuo
    :param candidato: Chromosome(Object)
    :param horaInicio: datetime
    :return: None
    """
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print("{}\t{}\t{}".format(
        ' '.join(candidato.getGenesStr()), candidato.Fitness, diferencia)
    )
