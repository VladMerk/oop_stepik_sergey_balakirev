class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __getitem__(self, indx):
        if 0 <= indx < len(self.points):
            return self.points[indx]
        raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self.points):
            raise IndexError('некорректный индекс')
        self.points[key][-1] = value

tr = Track(10, -5.4)
tr.add_point(20, 0, 100)
tr.add_point(50, -20, 80)
tr.add_point(63.45, 1.24, 60.34)
tr[2] = 60
print(tr.points)
