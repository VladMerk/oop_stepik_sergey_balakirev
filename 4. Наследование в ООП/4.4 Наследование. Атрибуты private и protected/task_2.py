class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __verify_name(self, s):
        if not isinstance(s, str):
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, value):
        if value <= 0:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
