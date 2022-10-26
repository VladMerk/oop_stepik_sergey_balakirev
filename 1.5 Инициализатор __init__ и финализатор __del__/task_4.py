# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        attrs = [self.a, self.b, self.c]
        filtred_types = list(filter(lambda x:
                                    type(x) not in (int, float) or x <= 0, attrs))

        if bool(filtred_types):
            return 1

        attrs = sorted(attrs)
        return 3 if attrs[0] + attrs[1] > attrs[2] else 2


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle()
#  с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
