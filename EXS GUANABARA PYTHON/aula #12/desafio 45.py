import random
lista = [0, 1, 2]
print("SUAS OPÇÕES: ")
print("[0] PEDRA")
print("[1] TESOURA")
print("[2] PAPEL")
jogada = int(input("qual é a sua jogada: "))
computa = random.choice(lista)
if jogada == 0 and computa == 0:
    print("DEU EMPATE")
elif jogada == 0 and computa == 1:
    print("VOCE VENCEU, PEDRA > TESOURA")
elif jogada == 0 and computa == 2:
    print("VOCE PERDEU, PAPEL > PEDRA")
elif jogada == 1 and computa == 0:
    print("VOCE PERDEU, PEDRA > TESOURA")
elif jogada == 1 and computa == 1:
    print("DEU EMPATE")
elif jogada == 1 and computa == 2:
    print("VOCE GANHOU, TESOURA > PAPEL")
elif jogada == 2 and computa == 0:
    print("VOCE GANHOU, PAPEL > PEDRA")
elif jogada == 2 and computa == 1:
    print("VOCE PERDEU, TESOURA > PAPEL")
elif jogada == 2 and computa == 2:
    print("DEU EMPATE")
else:
    print("jogada invalida, tente novamente")