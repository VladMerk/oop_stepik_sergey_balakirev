class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, obj):
        w = self.width + obj.width
        h = self.height + obj.height
        d = self.depth + obj.depth
        return Box3D(w, h, d)

    def __mul__(self, value):
        w = self.width * value
        h = self.height * value
        d = self.depth * value
        return Box3D(w, h, d)

    def __rmul__(self, value):
        return self * value

    def __sub__(self, obj):
        w = self.width - obj.width
        h = self.height - obj.height
        d = self.depth - obj.depth
        return Box3D(w, h, d)

    def __floordiv__(self, value):
        w = self.width // value
        h = self.height // value
        d = self.depth // value
        return Box3D(w, h, d)

    def __mod__(self, value):
        w = self.width % value
        h = self.height % value
        d = self.depth % value
        return Box3D(w, h, d)


# Test
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

# Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 + box2
# Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = box1 * 2
box = 3 * box2    # Box3D: width=6, height=12, depth=18
# Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box2 - box1
# Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box1 // 2
box = box2 % 3    # Box3D: width=2, height=1, depth=0
