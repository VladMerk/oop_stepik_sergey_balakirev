class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step >= self.stop:
            raise StopIteration
        self.value += self.step
        return self.value

class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value >= self.rows:
            raise StopIteration
        self.value += 1
        return iter(self.fr)



fr = FRange2D(0, 2, 0.5)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()
