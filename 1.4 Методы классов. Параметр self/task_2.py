class Graph:

    def set_data(self, data):
        self.data = data
        self.LIMIT_Y = [0, 10]

    def draw(self):
        for item in self.data:
            if self.LIMIT_Y[0] <= item <= self.LIMIT_Y[1]:
                print(item, end=' ')
        print()

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
