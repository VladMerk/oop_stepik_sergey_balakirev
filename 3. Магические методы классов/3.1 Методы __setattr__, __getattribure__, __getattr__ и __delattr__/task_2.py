class Product:
    _count = 0

    def __new__(cls, *args):
        cls._count += 1
        return super().__new__(cls)

    def __init__(self, name='', weight=0, price=0):
        self.id = self._count
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'id' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'weight' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'price' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['weight', 'price'] and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, key)

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

# Test
if __name__ == "__main__":
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", -150, 512))
    for p in shop.goods:
        print(f"{p.id}, {p.name}, {p.weight}, {p.price}")
