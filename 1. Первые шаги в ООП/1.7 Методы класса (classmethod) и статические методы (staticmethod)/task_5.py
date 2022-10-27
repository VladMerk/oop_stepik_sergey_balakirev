class AppStore:
    def __init__(self) -> None:
        self.apps = {}

    def add_application(self, app):
        self.apps[app.name] = app

    def remove_application(self, app):
        if app.name in self.apps:
            del self.apps[app.name]
        else:
            print('Нет такого приложения в AppStore')

    def block_application(self, app):
        self.apps[app.name].blocked = True

    def total_apps(self):
        return len(self.apps)


class Application:
    def __init__(self, name: str, blocked=False) -> None:
        self.name = name
        self.blocked = blocked
