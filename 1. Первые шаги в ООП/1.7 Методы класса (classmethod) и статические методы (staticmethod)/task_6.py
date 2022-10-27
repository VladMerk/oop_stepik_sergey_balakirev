class Message:
    def __init__(self, text: str, fl_like=False) -> None:
        self.text = text
        self.fl_like = fl_like


class Viber:
    _messages = []

    @classmethod
    def add_message(cls, msg: Message):
        cls._messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls._messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        indx = cls._messages.index(msg)
        cls._messages[indx].fl_like = not cls._messages[indx].fl_like

    @classmethod
    def show_last_message(cls, num):
        for item in cls._messages[-num:]:
            print(item.text)

    @classmethod
    def total_messages(cls):
        return len(cls._messages)
