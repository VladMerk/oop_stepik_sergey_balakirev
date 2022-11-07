class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= value < self.MAX_DIMENSION:
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= value < self.MAX_DIMENSION:
            self.__b = value

    @property
    def c(self):
        return self.__c

    @b.setter
    def c(self, value):
        if self.MIN_DIMENSION <= value < self.MAX_DIMENSION:
            self.__c = value

    @classmethod
    def __volume(cls, obj):
        return obj.a * obj.b * obj.c

    def __ge__(self, other):
        return __class__.__volume(self) >= __class__.__volume(other)

    def __gt__(self, other):
        return __class__.__volume(self) > __class__.__volume(other)


class ShopItem:
    def __init__(self, name, price, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [
    ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
    ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
    ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
    ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
