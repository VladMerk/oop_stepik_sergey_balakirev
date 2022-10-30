class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if not list(filter(lambda x: type(x) == type(app), self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)
        self.apps_type.remove(type(app))

class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'

class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list

if __name__ == "__main__":
    sm = SmartPhone("Honor 1.0")
    sm.add_app(AppVK())
    sm.add_app(AppVK())  # второй раз добавляться не должно
    sm.add_app(AppYouTube(2048))
    for a in sm.apps:
        print(a.name)

