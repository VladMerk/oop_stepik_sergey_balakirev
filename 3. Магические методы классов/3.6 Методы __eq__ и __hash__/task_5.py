class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if float(value) <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return super().__setattr__(key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)

s = "1 2 3; 4 5 6.78; 1 2 3; 4 1 2.5".split(';')
lst_dims = []
for item in s:
    a, b, c = item.split()
    lst_dims.append(Dimensions(a, b, c))

lst_dims.sort()
print(lst_dims)
