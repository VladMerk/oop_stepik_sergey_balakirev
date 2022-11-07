class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_mass(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.get_mass() == other.get_mass()
        return self.get_mass() == other

    def __gt__(self, other):
        if isinstance(other, Body):
            return self.get_mass() > other.get_mass()
        return self.get_mass() > other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.get_mass() < other.get_mass()
        return self.get_mass() < other
