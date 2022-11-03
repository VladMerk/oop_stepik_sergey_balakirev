class ObjList:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def __call__(self, indx):
        return self.linked_lst(indx)

    def add_obj(self, obj: ObjList):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.head:
            self.head = obj
        self.lenght += 1

    def remove_obj(self, indx):
        node = self.head
        i = 0

        while node and i < indx:
            node = node.next
            i += 1
        if node is None:
            return

        p, n = node.prev, node.next
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == node:
            self.head = n
        if self.tail == node:
            self.tail = p


        self.lenght -= 1


    def __len__(self):
        return self.lenght

    def linked_lst(self, indx):
        i = 0
        node = self.head
        while i < indx:
            node = node.next
            i += 1
        return node.data

# Добавил реализацию __iter__ как отдельное задание чтобы можно использовать циклы
    def __iter__(self):
        node = self.head

        while node:
            yield node.data
            node = node.next

if __name__ == "__main__":
    dbList = LinkedList()
    dbList.add_obj(ObjList("Sergey"))
    dbList.add_obj(ObjList("Balakirev"))
    dbList.add_obj(ObjList("Python"))

    for e in dbList:
        print(e, end=" ")

    print()
    print(len(dbList))
    print()
    dbList.remove_obj(0)
    for e in dbList:
        print(e, end=" ")
    print()
    print(len(dbList))
    print(dbList.linked_lst(1))
    print(dbList(1))
