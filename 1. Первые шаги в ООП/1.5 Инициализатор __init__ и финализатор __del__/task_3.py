import random


class Point:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Point):
    pass


class Rect(Point):
    pass


class Ellipse(Point):
    pass


elements = []
for _ in range(217):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    elements.append(random.choice(
        [Line(0, 0, 0, 0),
         Rect(a, b, c, d),
         Ellipse(a, b, c, d)]))
