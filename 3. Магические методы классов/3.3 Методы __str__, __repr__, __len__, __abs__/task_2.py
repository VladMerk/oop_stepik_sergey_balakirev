class Model:
    def __init__(self):
        self.filds = {}

    def query(self, **kwargs):
        # self.filds = dict(key:value for (key, value) in **kwargs.items())
        self.filds = kwargs

    def __repr__(self) -> str:
        return 'Model' + ': ' + ', '.join(f'{k} = {v}' for k, v in self.filds.items()) if self.filds else "Model"


model = Model()
model.query(id=1, fio='fio', old=33)
print(model)
