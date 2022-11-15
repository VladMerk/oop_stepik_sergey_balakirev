class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def get_coords(self):
        return tuple(self.coords)

    def _verify(self, a, b):
        if len(a) != len(b):
            raise TypeError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if self._verify(self, other):
            m = list(map(lambda x,y: x+y, self.coords, other.coords))
            return Vector(*m)

    def __sub__(self, other):
        if self._verify(self, other):
            m = list(map(lambda x,y: x - y, self.coords, other.coords))
            return Vector(*m)


class VectorInt(Vector):
    def __init__(self, *args):
        for x in args:
            if isinstance(x, float):
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def _verify_type_int(self, lst):
        return not any(isinstance(x, float) for x in lst)

    def __add__(self, other):
        return VectorInt(*list(map(lambda x, y: x + y, self.coords, other.coords))) \
            if self._verify_type_int(other.coords) else super().__add__(other)

    def __sub__(self, other):
        return VectorInt(*list(map(lambda x, y: x - y, self.coords, other.coords))) \
            if self._verify_type_int(other) else super().__sub__(other)

# Test
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"


v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1+v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1+v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
