class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []
unique_books = 0
for row in lst_in:
    name, author, year = row.split(';')
    item = BookStudy(name, author, year)
    if item not in lst_bs:
        unique_books += 1
    lst_bs.append(item)

print(unique_books)
print(lst_bs)
print(len(lst_bs))
print(len(set(lst_bs)))
