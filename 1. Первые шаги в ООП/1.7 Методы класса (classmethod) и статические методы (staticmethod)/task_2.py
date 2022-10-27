from string import ascii_lowercase, digits
import re

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        return 3 < len(name) < 50 and bool(re.match(r'[A-Za-zА-Яа-я0-9]+', name))

    def __new__(cls, name):
        if cls.check_name(name):
            return super().__new__(cls)
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10) -> None:
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        return 3 <= len(name) < 50 and bool(re.match(r'[A-Za-zА-Яа-я0-9]+', name))

    def __new__(cls, name):
        if cls.check_name(name):
            return super().__new__(cls)
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10) -> None:
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
