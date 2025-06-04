from random import randint
from operator import itemgetter
jogada = {}
c = 0
for i in range(0, 4):
    c = c + 1
    jogada[f'jogador{c}'] = (randint(1, 6))
c = 0
ranking = {}
for k, v in jogada.items():
    c = c + 1
    print(f"jogador{c} tirou {v}")
print('RANKING =-=-=-=-=-==-==--==-=-==-')
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print(ranking)

