class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args):
        if cls.__count < 5:
            cls.__count += 1
            cls.__instance =  super().__new__(cls)
        return cls.__instance

    def __init__(self, name) -> None:
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
