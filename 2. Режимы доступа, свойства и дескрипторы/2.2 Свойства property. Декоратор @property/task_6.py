from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class PathLines:
    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        return self.lines

    def get_length(self):
        lines = [LineTo()] + self.lines
        return sum(sqrt(((lines[i + 1].x - lines[i].x) ** 2 + (lines[i + 1].y - lines[i].y) ** 2)) for i in range(len(lines) - 1))

    def add_line(self, line):
        self.lines.append(line)
