"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name functions
"""
import datetime
from .board import Board
from .aptitud import Fitness


def getFitnessByGenes(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for row in range(size):
        for col in range(size):
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastDiagonalsWithQueens.add(row + col)
                southEastDiagonalsWithQueens.add(size - 1 - row + col)
    total = size - len(rowsWithQueens) \
            + size - len(colsWithQueens) \
            + size - len(northEastDiagonalsWithQueens) \
            + size - len(southEastDiagonalsWithQueens)
    return Fitness(total)


def printBoard(individuo, startTime, size):
    calculate_difference = (datetime.datetime.now() - startTime)  # Total  de segGuntdos
    board = Board(individuo.getGenes(), size)
    board.print()
    print("{}\t- {}\t{}".format(
        ' '.join(map(str, individuo.getGenes())),
        individuo.Fitness,
        calculate_difference))
