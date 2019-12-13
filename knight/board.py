"""
@author miguelCabrera1001 | 
@date 12/12/19
@project 
@name board
"""


class Board:
    def __init__(self, positions, width, height):
        board = [['.'] * width for _ in range(height)]
        for index in range(len(positions)):
            positionKnigh = positions[index]
            # print(positionKnigh)
            board[positionKnigh.Y][positionKnigh.X] = 'K'
        self._board = board
        self.width = width
        self.height = height

    def print(self):
        """
        :return:
        """
        # {0,0}  es la esquina inferior derecha
        for i in reversed(range(self.height)):
            print(i, '\t', ' '.join(self._board[i]))
        print("\t", " ".join(map(str, range(self.width))))
