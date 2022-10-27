from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + '_.@'
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False
        s = email.split("@")
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        return False if '.' not in s[1] else '..' not in email

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)]
                       for _ in range(n)) + '@gmail.com'
