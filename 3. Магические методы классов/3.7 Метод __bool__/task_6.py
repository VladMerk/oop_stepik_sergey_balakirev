class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __eq__(self, other):
        return all(list(map(lambda x,y: x == y, self.coords, other.coords)))

    def __len__(self):
        return len(self.coords)

    def _verify(self, a, b):
        if len(a) != len(b):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if self._verify(self, other):
            m = list(map(lambda x,y: x+y, self.coords, other.coords))
            return Vector(*m)

    def __iadd__(self, other):
        if type(other) in [int, float]:
            for i in range(len(self.coords)):
                self.coords[i] += other
            return self
        if type(other) == Vector:
            if self._verify(self, other):
                m = self.__add__(other).coords
            return Vector(*m)

    def __sub__(self, other):
        if self._verify(self, other):
            m = list(map(lambda x,y: x - y, self.coords, other.coords))
            return Vector(*m)

    def __isub__(self, other):
        if type(other) in [int, float]:
            for i in range(len(self.coords)):
                self.coords[i] -= other
            return self
        if type(other) == Vector:
            if self._verify(self, other):
                m = self.__sub__(other).coords
            return Vector(*m)

    def __mul__(self, other):
        if self._verify(self, other):
            m = list(map(lambda x,y: x * y, self.coords, other.coords))
        return Vector(*m)


# Test
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)
print((v1 - v2).coords)
print((v1 * v2).coords)

v1 += 10
print(v1.coords)
v1 -= 10
print(v1.coords)
v1 += v2
print(v1.coords)
v2 -= v1
print(v2.coords)

print(v1 == v2)
print(v1 != v2)
