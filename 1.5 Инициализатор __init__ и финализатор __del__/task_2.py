class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1, 2000, 2):
    if i == 3:
        points.append(Point(i, i, 'yellow'))
    else:
        points.append(Point(i, i))
