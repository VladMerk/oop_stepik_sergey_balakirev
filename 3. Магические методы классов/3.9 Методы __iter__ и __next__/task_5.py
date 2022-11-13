class Cell:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.type_data = type_data
        self.rows = rows
        self.cols = cols
        self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def _check_item(self, item):
        if item[0] < 0 or item[0] >= len(self.table):
            raise IndexError('неверный индекс')
        if item[1] < 0 or item[1] >= len(self.table[0]):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self._check_item(item)
        return self.table[item[0]][item[1]]

    def __setitem__(self, item, value):
        self._check_item(item)
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
        self.table[item[0]][item[1]] = value

    def __iter__(self):
        for i in range(self.cols):
            yield [item.data for item in self.table[i]]


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
