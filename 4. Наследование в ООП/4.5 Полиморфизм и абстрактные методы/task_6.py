from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError()

        self.__name = value

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError()
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError()
        self.__square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
