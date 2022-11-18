class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self.__points.append(PointTrack(*args))
        else:
            self.__points.extend(args)

    @property
    def points(self):
        return tuple(self.__points)


    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.points

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
