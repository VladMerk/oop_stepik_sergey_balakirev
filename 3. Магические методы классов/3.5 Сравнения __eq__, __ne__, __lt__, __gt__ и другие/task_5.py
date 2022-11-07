class FileAcceptor:
    def __init__(self, *args):
        self.file_ends = list(args)

    def __eq__(self, filename: str):
        return filename.split('.')[-1] in self.file_ends

    def __call__(self, filename):
        return filename == self
        # return filename.endswith(self.extensions)

    def __add__(self, obj):
        return FileAcceptor(*set(self.file_ends + obj.file_ends))


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]


acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))

print(filenames)
