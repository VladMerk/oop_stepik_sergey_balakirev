class SoftList(list):

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except Exception:
            return False

sl = SoftList('python')
print(sl[0])
print(sl[-1])
print(sl[6])
print(sl[-7])
