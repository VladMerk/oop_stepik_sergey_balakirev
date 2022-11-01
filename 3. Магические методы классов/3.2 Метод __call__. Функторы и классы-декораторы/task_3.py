class LengthValidator:
    def __init__(self, min_lenght, max_lenght):
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def __call__(self, *args, **kwargs):
        return len(args[0]) in range(self.min_lenght, self.max_lenght+1)


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return all(char in self.chars for char in args)


# Test
lv = LengthValidator(3, 50)
res = lv('12345')
print(res)
