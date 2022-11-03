class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def get_coords(self):
        return self.coords

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

# Test
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly.get_coords())
poly.add_coord(4, 10)
print(poly.get_coords())
poly.remove_coord(2)
print(poly.get_coords())
