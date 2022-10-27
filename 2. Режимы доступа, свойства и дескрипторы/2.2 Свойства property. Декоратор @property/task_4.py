class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0) -> None:
        if type(x) in [int, float] and RadiusVector2D.MIN_COORD < x < RadiusVector2D.MAX_COORD:
            self.__x = x
        else:
            self.__x = 0

        if type(x) in [int, float] and RadiusVector2D.MIN_COORD < y < RadiusVector2D.MAX_COORD:
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in [int, float] and RadiusVector2D.MIN_COORD < x < RadiusVector2D.MAX_COORD:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in [int, float] and __class__.MIN_COORD < y < __class__.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.y ** 2 + vector.x**2
