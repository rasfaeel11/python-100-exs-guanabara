from random import randint
jogador = 0
computador = 0
s = 0
countvit = 0
print("JOGO PAR OU IMPAR: JOGADOR VS COMPUTADOR EDITION")
print("=================================================")
while True:
    jogador = int(input("digite um valor: "))
    par_ou_impar = str(input("voce quer par ou impar: (p, I): ")).strip().lower()
    computador = randint(0, 15)
    s = computador + jogador
    if par_ou_impar == "p":
        res = s % 2 
        if res == 0:
            print(f"a soma dos numeros foi {s} e esse numero e PAR")
            print("JOGADOR VENCEU")
            countvit = countvit + 1
        else:
             print(f"a soma dos numeros foi {s} e esse numero e IMPAR")
             print("JOGADOR PERDEU")
             break
    if par_ou_impar == "i":
        res = s % 2
        if res == 1:
            print(f"a soma dos numeros foi {s} e esse numero e IMPAR")
            print("JOGADOR VENCEU")
            countvit = countvit + 1
        else:
             print(f"a soma dos numeros foi {s} e esse numero e PAR")
             print("JOGADOR PERDEU")
             break
print(f"o jogador venceu: {countvit}")