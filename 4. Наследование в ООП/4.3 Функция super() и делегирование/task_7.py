class StringDigit(str):
    def __init__(self, string: str):
        self.__check_string(string)
        super().__init__()

    def __check_string(self, string: str):
        if not all((i.isdigit() for i in string)):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other: str):
        self.__check_string(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other: str):
        return StringDigit(other).__add__(self)



sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

