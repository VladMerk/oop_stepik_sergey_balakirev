class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def get_weight(self):
        return sum(x.weight for x in self.things)

    def add_thing(self, thing):
        if self.get_weight() + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

        self.things.append(thing)

    def _verify(self, item):
        if item < 0 or item >= len(self.things):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self._verify(item)
        return self.things[item]

    def __setitem__(self, item, value):
        self._verify(item)
        if self.get_weight() - self.things[item].weight + value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things[item] = value

    def __delitem__(self, item):
        self._verify(item)
        self.things.pop(item)

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
