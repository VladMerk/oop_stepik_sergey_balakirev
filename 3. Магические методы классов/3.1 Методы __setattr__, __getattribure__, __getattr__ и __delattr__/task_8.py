class BaseFilter:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date':
            if hasattr(self, key):
                return
            if type(value) not in [float, int]:
                return
            if value <= 0:
                return
        object.__setattr__(self, key, value)


class Mechanical(BaseFilter):
    pass


class Aragon(BaseFilter):
    pass


class Calcium(BaseFilter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    d = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self) -> None:
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if self.d[slot_num] == type(filter):
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all(i != None and 0 <= time.time() - i.date <= self.MAX_DATE_FILTER for i in self.slots)


# Test
if __name__ == "__main__":
    import time

    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))

    assert my_water.water_on(
    ) == False, "метод water_on вернул True, хотя не все фильтры были установлены"

    my_water.add_filter(3, Calcium(time.time()))
    assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

    f1, f2, f3 = my_water.get_filters()
    assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(
        f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

    my_water.remove_filter(1)
    assert my_water.water_on(
    ) == False, "метод water_on вернул True, хотя один из фильтров был удален"

    my_water.add_filter(1, Mechanical(time.time()))
    assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

    f1, f2, f3 = my_water.get_filters()
    my_water.remove_filter(1)

    my_water.add_filter(1, Mechanical(
        time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
    assert my_water.water_on(
    ) == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

    f1 = Mechanical(1.0)
    f2 = Aragon(2.0)
    f3 = Calcium(3.0)
    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

    f1.date = 5.0
    f2.date = 5.0
    f3.date = 5.0

    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
