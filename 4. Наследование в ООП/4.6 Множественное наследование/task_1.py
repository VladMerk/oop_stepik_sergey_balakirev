class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Positive(Digit):
    def __init__(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Negative(Digit):
    def __init__(self, value):
        if not isinstance(value, (int, float)) or value > 0:
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2),
          FloatPositive(6.5), FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
