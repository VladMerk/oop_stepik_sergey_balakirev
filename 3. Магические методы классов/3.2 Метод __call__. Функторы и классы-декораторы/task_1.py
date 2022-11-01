import random


class RandomPassword:
    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def __call__(self, *args, **kwards):
        lst = random.randint(self.min_lenght, self.max_lenght)
        return ''.join([random.choice(self.psw_chars) for _ in range(lst)])


min_lenght = 5
max_lenght = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_lenght, max_lenght)
psw = rnd()
lst_pass = [psw for _ in range(3)]

# Test
print(lst_pass)
