class Morph:
    def __init__(self, *args):
        self.lst_words = list(args)

    def add_word(self, word):
        self.lst_words.append(word)

    def get_words(self):
        return tuple(self.lst_words)

    def __eq__(self, word):
        return word.lower() in self.lst_words


dict_words = [
    Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
    Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
]

# Test
text = 'Мы будем устанавливать связь завтра днем.'

print(sum(bool(word) for word in text.strip(' .').split() if word in dict_words))
