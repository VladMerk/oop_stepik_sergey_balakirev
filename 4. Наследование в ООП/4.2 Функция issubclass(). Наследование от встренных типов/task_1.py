class ListInteger(list):
    def __init__(self, lst):
        for x in lst:
            if self._verify(x):
                continue
        super().__init__(lst)


    def _verify(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        return True

    def __setitem__(self, item, value):
        if self._verify(value):
            super().__setitem__(item, value)

    def append(self, value):
        if self._verify(value):
            super().append(value)

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError
s[0] = 10
print(s)
