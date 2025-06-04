pesomenor = 0
pesomaior = 0
for c in range(0, 3):
    peso = float(input("digite o peso da pessoa: "))
    if c == 0:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        if pesomenor > peso: #se o MENOR PESO for MAIOR que o PESO, ele vira menor peso # AQUI E OUTRO IF PQ TA DENTRO DO ELSE
            pesomenor = peso
print(pesomaior)
print(pesomenor)