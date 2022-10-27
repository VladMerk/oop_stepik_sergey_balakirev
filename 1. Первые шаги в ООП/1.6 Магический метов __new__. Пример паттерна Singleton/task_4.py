class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(2, 5)
pt_clone = pt.clone()
