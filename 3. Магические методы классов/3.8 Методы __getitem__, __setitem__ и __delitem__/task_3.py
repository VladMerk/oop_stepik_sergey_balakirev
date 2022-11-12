class Integer:
    def __init__(self, start_value = 0):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self.__value = val


class Array:
    def __init__(self, max_lenght, cell=Integer):
        self.items = [cell() for _ in range(max_lenght)]

    def __repr__(self) -> str:
        return ' '.join(str(x.value) for x in self.items)

    def  __getitem__(self, key):
        if isinstance(key, int) and key >= 0 and key < len(self.items):
            return self.items[key].value
        raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, val):
        if not isinstance(key, int) and key < 0 and key >= len(self.items):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.items[key].value = val


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)
ar_int[1] = 10
ar_int[9] = 8
print(ar_int)
