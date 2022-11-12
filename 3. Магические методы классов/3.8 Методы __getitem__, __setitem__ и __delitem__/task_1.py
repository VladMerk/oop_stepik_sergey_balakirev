class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, key):
        if 0 <= key < len(self.__dict__.keys()) and isinstance(key, int):
            return self.__dict__[list(self.__dict__.keys())[key]]
        raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.__dict__.keys()) and isinstance(key, int):
            self.__dict__[list(self.__dict__.keys())[key]] = value
        else:
            raise IndexError('неверный индекс поля')


r = Record(pk=2, title='Python', author='Author')
print(r.__dict__)
r[2] = 'Балакирев'
print(r.__dict__)
print(r[0], r[1])
