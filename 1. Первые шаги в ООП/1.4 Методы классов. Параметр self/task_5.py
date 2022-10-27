class Translator:

    trans = dict()

    def add(self, eng, rus):

        if eng not in self.trans:
            self.trans[eng] = [rus]

        if rus not in self.trans[eng]:
            self.trans[eng] += [rus]

    def remove(self, eng):
        del self.trans[eng]

    def translate(self, eng):
        return self.trans[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.add('digits', '1')
tr.add('digits', '2')
tr.add('digits', '1')

tr.remove('car')
print(*tr.translate('go'), end=' ')
