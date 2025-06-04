import random
n = random.randint(0, 5)
n2 = int(input("digite qualquer valor: "))
if n2 == n:
    print("voce ganhou!")
else:
    print('voce perdeu parca')
print(f"o numero escolhido pelo pc foi: {n}")