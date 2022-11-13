class TriangleListIterator:
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(i+1):
                yield self._lst[i][j]

    