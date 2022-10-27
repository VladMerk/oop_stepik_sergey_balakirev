class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if type(value) in [int, float]:
            self.__weight = value


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if sum(a.weight for a in self.__things) + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.remove(indx)

    def get_total_weight(self):
        return sum(a.weight for a in self.__things)


# Test
if __name__ == "__main__":
    bag = Bag(1000)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    w = bag.get_total_weight()
    for t in bag.things:
        print(f"{t.name}: {t.weight}")
