class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return all(hasattr(self, x) for x in ['x1', 'y1', 'x2', 'y2'])

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(), Ellipse(5, 6, 7, 8)]

for item in lst_geom:
    if item:
        item.get_coords()
