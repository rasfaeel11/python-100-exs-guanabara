import random
jogos = int(input("quantos jogos voce quer gerar: "))
for i in range(jogos):
    numeros = random.sample(range(60), 6)
    numeros.sort()
    print(f"JOGO {i + 1}: {numeros}")