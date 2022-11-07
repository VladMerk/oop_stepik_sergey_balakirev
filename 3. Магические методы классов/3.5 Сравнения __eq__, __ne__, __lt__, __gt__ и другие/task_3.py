import re

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]
lst_words = [re.sub(r"[–?!,.;]", '', a).split() for a in stich]

class StringText:
    def __init__(self, lst_words: list):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __gt__(self, other):
        return len(self.lst_words) > len(other)

    def __ge__(self, other):
        return len(self.lst_words) >= len(other)

lst_text = [StringText(a) for a in lst_words]
lst_text_sorted = [' '.join(a.lst_words) for a in sorted(lst_text, reverse=True)]

# Test
print(lst_text_sorted)
