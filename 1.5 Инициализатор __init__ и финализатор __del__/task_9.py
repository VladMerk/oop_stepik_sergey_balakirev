import itertools
import random


class Cell:
    def __init__(self, around_mines=0, mine=False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M) -> None:
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def init(self):
        m = 0
        while m < self.M:
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1),\
                            (0, 1), (1, -1), (1, 0), (1, 1)
        for x, y in itertools.product(range(self.N), range(self.N)):
            if not self.pole[x][y].mine:
                mines = sum((self.pole[x + i][y + j].mine for i,
                            j in indx if 0 <= x+i < self.N and 0 <= y+j < self.N))
                self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: ('*' if x.mine else x.around_mines)
                                        if x.fl_open else '#', row))


pole_game = GamePole(10, 12)
