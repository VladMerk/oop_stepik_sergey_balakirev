class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]




lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
