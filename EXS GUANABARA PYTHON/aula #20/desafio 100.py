from random import randint

lista = []

def sorteio():
    for i in range(0, 5):
        lista.append(randint(1, 20))
    print('sorteando os valores pares da lista:', lista)

def pares():
    soma = 0
    for i, v in enumerate(lista): 
        if v % 2 == 0:
            soma = soma + v
    print(f'a soma da lista {lista} foi: {soma}')

sorteio()
pares()