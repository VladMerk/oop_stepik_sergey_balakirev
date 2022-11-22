class Note:
    def __init__(self, name, ton):
        self.__notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
        self._name = name
        self._ton = ton


    def __setattr__(self, key, value):
        if key == '_name' and value not in self.__notes:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in [-1, 0, 1]:
            raise ValueError('недопустимое значение аргумента')
        return super().__setattr__(key, value)

class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Notes, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        if not isinstance(item, int) or item not in range(7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])

notes = Notes()
