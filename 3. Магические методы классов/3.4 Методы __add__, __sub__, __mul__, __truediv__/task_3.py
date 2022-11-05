class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            h = self.top
            while h.next is not None:
                h = h.next

            h.next = obj

    def pop_back(self):
        prev = None
        h = self.top
        while h.next is not None:
            prev = h
            h = h.next

        prev.next = None

    def __add__(self, obj):
        self.push_back(obj=obj)
        return self

    def __mul__(self, lst):
        for item in lst:
            self.push_back(StackObj(item))

        return self

    def __repr__(self):
        swap = []
        h = self.top
        while h is not None:
            swap.append(h.data)
            h = h.next
        return ", ".join(str(x) for x in swap).rstrip()


# Test
assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
