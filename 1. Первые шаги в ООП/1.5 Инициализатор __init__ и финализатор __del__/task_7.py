# здесь пишите программу
class Gadget:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Table(Gadget):
    pass


class TV(Gadget):
    pass


class Notebook(Gadget):
    pass


class Cup(Gadget):
    pass


class Cart:
    def __init__(self, goods=list()):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


cart = Cart()
cart.add(TV('LG', 23000))
cart.add(TV('Samsung', 35000))
cart.add(Table('Стол деревянный', 5000))
cart.add(Notebook('Samsung', 60000))
cart.add(Notebook('Huawey', 55000))
cart.add(Cup('Кружка красная', 500))
