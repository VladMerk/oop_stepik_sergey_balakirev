import random
import itertools

class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = value


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or value not in range(9):
            raise ValueError("недопустимое значение атрибута")

        self.__number = value


    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")

        self.__is_open = value

    def __bool__(self):
        return not self.is_open


class GamePole:
    _isinstance = None
    def __new__(cls, *args, **kwargs):
        if cls._isinstance is None:
            cls._isinstance = object.__new__(cls)
        return cls._isinstance

    def __init__(self, n, m, total_mines):
        self.N = n
        self.M = m
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.M)] for _ in range(self.N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
# Расставляем мины по полю в случайном порядке
        m = 0
        while m < self.total_mines:
# цикл пока не достигнет нужного количества мин
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if self.pole[i][j].is_mine:
                # если мина в этом поле уже есть, просто продолжаем цикл
                continue
            self.pole[i][j].is_mine = True # иначе устанавливаем мину
            m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1),\
                            (0, 1), (1, -1), (1, 0), (1, 1) # индексы для обхода клеток
        for x, y in itertools.product(range(self.N), range(self.M)):
            # перебираем все клетки и считаем мины вокруг нее
            if not self.pole[x][y].is_mine:
                mines = sum((self.pole[x+i][y+j].is_mine
                for i,j in indx if 0 <= x+i < self.N and 0 <= y+j < self.M))
            self.pole[x][y].number = mines # после подсчета, устанавливаем количество мин в клетку.

    def open_cell(self, i, j):
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: ('*' if x.is_mine else x.number)
                            if x.is_open else '#', row))



# --------------------------------/Tests/----------------------------------

# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert not bool(cell), "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k, l in itertools.product(range(-1, 2), range(-1, 2)):
        ii, jj = k+i, l+j
        if ii < 0 or ii > 9 or jj < 0 or jj > 19:
            continue
        if pole[ii][jj].is_mine:
            n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
