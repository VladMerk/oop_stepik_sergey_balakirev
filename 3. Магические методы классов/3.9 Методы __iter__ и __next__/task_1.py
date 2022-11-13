class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.data = [self.fio, self.job, self.old, self.salary, self.year_job]

    def _check_indx(self, indx):
        if type(indx) != int or indx not in [0, 1, 2, 3, 4]:
            raise IndexError('неверный индекс')

    def __getitem__(self, indx):
        self._check_indx(indx)
        return self.data[indx]

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        self.data[indx] = value


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
