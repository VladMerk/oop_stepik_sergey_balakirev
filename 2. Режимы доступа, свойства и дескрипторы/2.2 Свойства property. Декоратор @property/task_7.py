class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    def _is_number(self, number):
        return bool(number // 10000000000)

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if self._is_number(number=value):
            self.__number = value
        else:
            print('Должно быть число из 11 цифр')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value


class PhoneBook:
    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        del self.phone_list[indx]

    def get_phone_list(self):
        return self.phone_list
