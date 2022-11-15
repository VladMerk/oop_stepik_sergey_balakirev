class Tuple(tuple):

    def __add__(self, other):
        m = tuple(self) + tuple(other) if len(other) else tuple(self) + other
        return Tuple(m)

