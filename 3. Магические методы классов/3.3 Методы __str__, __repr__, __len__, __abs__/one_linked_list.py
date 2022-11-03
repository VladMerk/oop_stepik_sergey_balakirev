"""
Самостоятельная реализация односвязного списка на основе "task_4.py"
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, obj):
        obj = Node(obj)
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.head:
            self.head = obj

    def pop(self):
        node = self.head
        prev = None
        while node.next is not None:
            prev = node
            node = node.next

        prev.next = None
        self.tail = prev
        return node.data

    def delete(self, value):
        node = self.head
        prev = None
        while node is not None and node.data != value:
            prev = node
            node = node.next

        prev.next = node.next

    def bpop(self):
        self.head = self.head.next


    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        lst = []
        node = self.head
        while node:
            lst.append(str(node.data))
            node = node.next
        return ', '.join(lst).rstrip()


lst = LinkedList()
lst.add(5)
lst.add(35)
print(lst)
lst.add(65)
print(lst)
print(lst.pop())
print(lst)
lst.add(77)
lst.add(93)
lst.add(12)
print(lst)
lst.delete(77)
print(lst)
lst.bpop()
print(lst)
lst.bpop()
print(lst)
