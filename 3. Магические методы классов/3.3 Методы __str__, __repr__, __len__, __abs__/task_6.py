import math


class RadiusVector:
    def __init__(self, *args):
        self.coords = [0] * args[0] if len(args) == 1 else list(args)

    def get_coords(self):
        return self.coords

    def set_coords(self, *args):
        for i, j in zip(range(len(self.coords)), args):
            self.coords[i] = j

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        sum_coords = sum(item ** 2 for item in self.coords)
        return math.sqrt(sum_coords)


# Test
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(a, b, c)
# ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(3, -5.6, 8, 10, 11)
print(vector3D.get_coords())
# ошибки быть не должно, меняются только первые две координаты
vector3D.set_coords(1, 2)
print(vector3D.get_coords())
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)
