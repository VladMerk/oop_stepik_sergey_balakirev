class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)

lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']

players = []
for row in lst_in:
    name, old, score = row.split(';')
    player = Player(name, int(old), int(score))
    players.append(player)

players_filtered = list(filter(bool, players))

print(players_filtered)
