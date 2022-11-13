class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if not self.top:
            self.top = obj
            return

        h = self.top
        while h.next is not None:
            h = h.next
        h.next = obj

    def push_front(self, obj):
        h = self.top
        obj.next = h
        self.top = obj

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __len__(self):
        h = self.top
        m = 0
        while h:
            m +=1
            h = h.next
        return m

    def _get_item(self, item):
        if item < 0 or item >= len(self):
            raise IndexError('неверный индекс')
        h = self.top
        m = 0
        if item == 0:
            return self.top

        while m < item:
            h = h.next
            m += 1

        return h

    def __getitem__(self, item):
        h = self._get_item(item)
        return h.data

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self):
            raise IndexError('неверный индекс')

        h = self._get_item(key)
        h.data = value



# Test
st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
