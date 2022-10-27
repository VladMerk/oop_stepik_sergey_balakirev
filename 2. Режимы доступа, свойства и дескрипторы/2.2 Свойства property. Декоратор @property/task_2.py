class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if 0 <= width <= 10000:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 0 <= height <= 10000:
            self.__height = height
            self.show()

    def show(self):
        print(f'{self.__title}: {self.width}, {self.height}')
