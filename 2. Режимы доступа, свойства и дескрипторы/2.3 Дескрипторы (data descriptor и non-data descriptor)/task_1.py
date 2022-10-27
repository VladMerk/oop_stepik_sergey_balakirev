import itertools


class FloatValue:
    @classmethod
    def verify(cls, value):
        if type(value) != float:
            raise TypeError(
                "Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)


class Cell:

    value = FloatValue()

    def __init__(self, value=0.0) -> None:
        self.value = value


class TableSheet:
    def __init__(self, N, M) -> None:
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]
        # для заполнения ячеек сразу от 1 до 15:
        # self.cells = [[Cell(float(i + 1 + j * M)) for i in range(M)] for j in range(N)]


N = 5
M = 3
table = TableSheet(N, M)
for count, (i, j) in enumerate(itertools.product(range(N), range(M)), start=1):
    table.cells[i][j] = Cell(float(count))

#Test
if __name__ == "__main__":

    assert isinstance(table, TableSheet)
    assert len(table.cells) == 5 and len(table.cells[0]) == 3

    assert type(table.cells) == list

    res = [int(x.value) for row in table.cells for x in row]
    assert res == list(range(1, 16))

    table.cells[0][0].value = 1.0
    x = table.cells[1][0].value

    try:
        table.cells[0][0].value = 'a'
    except TypeError:
        pass
    else:
        assert False, "не сгенерировалось исключение TypeError"
