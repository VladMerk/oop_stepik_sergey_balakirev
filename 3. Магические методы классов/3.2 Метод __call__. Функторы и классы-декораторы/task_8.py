class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return [int(item) for item in self.func().split(' ')]


input_dg = InputDigits(input)
res = input_dg()

