class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"

