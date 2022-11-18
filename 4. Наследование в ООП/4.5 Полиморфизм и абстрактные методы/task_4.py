from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return 'Базовый класс Model'

class ModelForm(Model):
    _count = 0
    def __new__(cls, *args, **kwargs):
        cls._count += 1
        return super().__new__(cls)

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self._count

    def get_pk(self):
        return self._id

form = ModelForm('Login', 'Password')
print(form.get_pk())
