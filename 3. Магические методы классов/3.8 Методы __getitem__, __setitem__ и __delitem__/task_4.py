class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f"__{name}"

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cell = cell
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, indx):
        return self.cells[indx[0]][indx[1]].value

    def __setitem__(self, indx, val):
        self.cells[indx[0]][indx[1]].value = val





table = TableValues(2, 3, cell=CellInteger)
print(table[1, 2])
table[1, 1] = 10
for row in table.cells:
    for x in row:
        print(x.value, end=" ")
    print()
