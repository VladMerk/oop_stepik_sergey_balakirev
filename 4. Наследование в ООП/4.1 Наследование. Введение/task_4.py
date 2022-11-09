class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton and cls._instance_base is None:
            cls._instance_base = object.__new__(cls)

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name
