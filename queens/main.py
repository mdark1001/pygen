"""
@author miguelCabrera1001 | 
@date 6/12/19
@project 
@name main
"""
import datetime

from  genetic import genetic
import unittest


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


class Board(object):
    """
        Se crea una clase para representar el tablero de ajedrez,
        Genes como indices de filas y columnas para representar la
        úbicación de las reinas en el tablero
    """

    def __init__(self, gen_set, size):
        self.gen_set = gen_set
        self.size = size
        self._board = self.getFirstBoard()

    def getFirstBoard(self):
        board = [['.'] * self.size for _ in range(self.size)]
        for index in range(0, len(self.gen_set), 2):
            row = self.gen_set[index]
            column = self.gen_set[index + 1]
            board[column][row] = 'Q'
        return board

    def print(self):
        """
        :return:
        """
        # {0,0}  es la esquina inferior derecha
        for i in reversed(range(len(self._board))):
            print(' '.join(self._board[i]))

    def get(self, row, column):
        return self._board[int(column)][int(row)]


class Fitness(object):
    def __init__(self, total):
        self.total = total

    def __gt__(self, other):
        return self.total < other.total

    def __str__(self):
        return "{}".format(self.total)


class TestQueens(unittest.TestCase):
    def main(self, size=8):
        """
        :param size:
        :return: False
        """
        genSet = self.generateGeneticSet(size)  # Inicializar el conjunto de Genes
        print(genSet)
        startTime = datetime.datetime.now()

        def fnDisplay(candidato):
            printBoard(candidato, startTime, size)

        def fnGetFitness(genes):
            return getFitnessByGenes(genes, size)

        optimo = Fitness(0)
        bestBoard = genetic.getBestChromosome(fitness=fnGetFitness,
                                              sizeTarget=2 * size,
                                              fitnessTarget=optimo,
                                              genSet=genSet,
                                              show=fnDisplay
                                              )
        self.assertTrue(not optimo > bestBoard.Fitness)

    def test_8(self):
        self.main(size=8)

    def test_16(self):
        self.main(size=16)

    def test_32(self):
        self.main(32)

    def generateGeneticSet(self, size):
        return [i for i in range(size)]


if __name__ == '__main__':
    unittest.main()
