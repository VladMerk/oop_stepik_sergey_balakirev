from string import ascii_lowercase, digits
import re


class CardCheck:
    @staticmethod
    def check_card_number(number):
        return bool(re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', number))

    @staticmethod
    def check_name(name):
        return bool(re.match(r'^[A-Z]+\s[A-Z]+$', name))
