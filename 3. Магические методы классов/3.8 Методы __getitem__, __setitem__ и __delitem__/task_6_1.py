class RadiusVector(list):
    def __getitem__(self, i):
        res = super().__getitem__(i)
        return tuple(res) if isinstance(res, list) else res

    def __init__(self, *args):
        super().__init__(args)




v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
