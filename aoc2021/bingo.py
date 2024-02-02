import numpy as np

class Bingo:
    def __init__(self, card) -> None:
        self.height = len(card)
        self.width = len(card[0])
        self.marked = np.tile(0, (self.height, self.width))
        self.card = np.array(card)
        self.won = False

    def set_marked(self, row, col) -> None:
        self.marked[row][col] = 1

    def is_winner(self) -> bool:
        if self.won:
            return True
        width1s = np.tile(1, self.width).tolist()
        height1s = np.tile(1, self.height).tolist()
        if width1s in self.marked.tolist():
            self.won = True
            return True
        elif height1s in self.marked.transpose().tolist():
            self.won = True
            return True
        else:
            return False
            
    def add_called(self, number) -> None:
        condition = self.card == number
        f_index = np.where(condition.ravel())
        element = np.take(self.marked, f_index)
        element = 1
        np.put(self.marked, f_index, element)

    def get_sum_unused(self) -> int:
        condition = self.marked == 0
        f_index = np.where(condition.ravel())
        element = np.take(self.card, f_index)
        tmp = np.tile(0, (self.height, self.width))
        np.put(tmp, f_index, element)
        return np.sum(tmp)

    def __repr__(self) -> str:
        return str(self.card)

