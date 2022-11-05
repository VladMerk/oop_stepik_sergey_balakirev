class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, value):
        self.book_list.append(value)
        return self

    def __sub__(self, value):
        if isinstance(value, int):
            self.book_list.pop(value)
            return self
        if isinstance(value, Book):
            self.book_list.remove(value)
            return self

    def __len__(self):
        return len(self.book_list)

    def __repr__(self) -> str:
        return self.book_list.__repr__()
