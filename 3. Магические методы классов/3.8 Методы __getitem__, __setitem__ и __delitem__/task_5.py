class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def __len__(self):
        a = 0
        h = self.top
        while h:
            a += 1
            h = h.next
        return a

    def push(self, obj):
        if not self.top:
            self.top = obj
            return

        h = self.top
        while h.next is not None:
            h = h.next

        h.next = obj

    def pop(self):
        if len(self) == 1:
            h = self.top
            self.top = None
            return h
        h = self.top
        prev = None
        while h.next:
            prev = h
            h = h.next

        prev.next = None
        return h

    def __getitem__(self, indx):
        if indx < 0 or indx >= len(self):
            raise IndexError('неверный индекс')

        h = self.top
        while indx:
            h = h.next
            indx -= 1

        return h

    def __setitem__(self, indx, value):
        if indx < 0 or indx > len(self):
            raise IndexError('неверный индекс')

        h = self.top
        while indx:
            h = h.next
            indx -= 1

        h.data = value.data

    def __iter__(self):
        h = self.top
        while h:
            yield h.data
            h = h.next

    def __repr__(self) -> str:
        lst = []
        h = self.top
        while h:
            lst.append(str(h.data))
            h = h.next
        return ', '.join(lst) or '[]'


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))

st[1] = StackObj('new obj2')
print(st[2].data)
print(st[1].data)
st.pop()
st.pop()
st.pop()
print(st)
