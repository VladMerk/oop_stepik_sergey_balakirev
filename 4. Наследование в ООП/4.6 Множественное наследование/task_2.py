class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id

class ShopGenericView:

    def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items()])

class ShopUserView:

    def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items() if key != '_id'])



class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year



book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022
