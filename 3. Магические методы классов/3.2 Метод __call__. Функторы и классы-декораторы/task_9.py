class RenderDigit:
    def __call__(self, string: str):
        try:
            return int(string)
        except Exception:
            return None

class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.render(item) for item in func().split(' ')]
        return wrapper


input_dg = InputValues(RenderDigit())(input)
res = input_dg()
# "1 -5.3 0.34 abc 45f -5"
print(res)
# [1, None, None, None, None, -5]
