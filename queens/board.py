"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name board
"""


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
