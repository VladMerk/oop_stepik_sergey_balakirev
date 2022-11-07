class BaseMoney:
    account = 'base'
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def valuate(self):
        if self.cb:
            return self.volume / self.cb.rates[self.account] * self.cb.rates['rub']
        raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        return round(self.valuate(),1) == round(other.valuate(), 1)

    def __ge__(self, other):
        return self.valuate() >= other.valuate()

    def __gt__(self, other):
        return self.valuate() > other.valuate()

class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money: BaseMoney):
        money.cb = cls

class MoneyR(BaseMoney):
    account = 'rub'

class MoneyD(BaseMoney):
    account = 'dollar'

class MoneyE(BaseMoney):
    account = 'euro'


# Test
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
