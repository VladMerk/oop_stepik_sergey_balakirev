import random
import os

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0  # True, если клетка свободна


class TicTacToe:

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.init()

    def init(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def __bool__(self):
        if self.is_human_win:
            return False
        if self.is_computer_win:
            return False
        if all(self[x, y] == 0 for y in range(len(self.pole[0])) for x in range(len(self.pole))):
            return True
        return True


    def _check_index(self, indx):
        for i in [0, 1]:
            if indx[i] < 0 or indx[i] not in range(3) or type(indx[i]) != int:
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self._check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, item, value):
        self._check_index(item)
        self.pole[item[0]][item[1]].value = value

    def show(self):
        for row in self.pole:
            for item in row:
                print(item.value, end=" ")
            print()

    def human_go(self):
        x, y = input("Введите 2 числа с координатам ячейки поля через пробел: ").split()
        if self[int(x), int(y)] == 0:
            self[int(x), int(y)] = TicTacToe.HUMAN_X

    def computer_go(self):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self[x, y] == 0:
                self[x, y] = TicTacToe.COMPUTER_O
                break

    def get_win(self, value):
        # по строкам
        for row in self.pole:
            if all(x.value == value for x in row):
                return True


        for col in range(len(self.pole[0])):
            a = [self.pole[row][col] for row in range(len(self.pole))]
            if all(x.value == value for x in a):
                return True

        if all(self[x, x] == value for x in range(len(self.pole))):
            return True

        return all((self[x, len(self.pole) - 1 - x] == value for x in range(len(self.pole))))

    @property
    def is_human_win(self):
        return self.get_win(TicTacToe.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.get_win(TicTacToe.COMPUTER_O)

    @property
    def is_draw(self):
        return not self and not self.is_human_win and not self.is_computer_win


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(
    cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert not bool(
    cell), "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(
    TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2,
                                2] == 0, "неверные значения ячеек, взятые по индексам"

game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1,
                                                  1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win == True and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game = TicTacToe()
game.init()
step_game = 0
while game:
    os.system('clear')
    game.show()
    print()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

os.system('clear')
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
