"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name functions
"""
import datetime
import random

from knight.posicion import Posicion
from knight.board import Board


def get_attacks(point, boardWidth, boardHeight):
    """
    Functión para obtener todas las casillas que podría atacar un caballo en una posición dada
    :param point: Position() Object
    :param boardWidth: Ancho del tablero
    :param boardHeight:  Alto del tablero
    :return: Lista de posibles ataques dada una posición en con las propiedades (x,y)
    """
    return [i for i in set(
        Posicion(x + point.X, y + point.Y)
        for x in [-2, -1, 1, 2] if 0 <= x + point.X < boardWidth
        for y in [-2, -1, 1, 2] if 0 <= y + point.Y < boardHeight
        and abs(y) != abs(x)

    )]


def create(fnPositionRandon, knight):
    """
    asignara un número específico de caballos a posiciones únicas del tablero
    :param fnPositionRamdon:
    :param knight:
    :return: List of genes
    """
    return [fnPositionRandon() for _ in range(knight)]


def mutate(genes, fnPositionRandon):
    """
    :param genes:
    :param fnPositionRamdon:
    :return:
    """
    cuenta = 2 if random.randint(0, 10) == 0 else 1
    while cuenta > 0:
        cuenta -= 1
        index = random.randrange(0, len(genes))
        genes[index] = fnPositionRandon()


def mostrar(candidato, horaInicio, tableroAncho, tableroAltura):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    tablero = Board(candidato.getGenes(), tableroAncho, tableroAltura)
    tablero.print()

    print("{}\n\t{}\t{}".format(
        ' '.join(candidato.getGenesStr()),
        candidato.getFitness(),
        diferencia))


def obtener_aptitud(genes, tableroAncho, tableroAltura):
    atacado = set(pos
                  for kn in genes
                  for pos in get_attacks(kn, tableroAncho, tableroAltura))
    return len(atacado)
