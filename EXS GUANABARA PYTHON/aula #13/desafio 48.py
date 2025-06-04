soma = 0
countc = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        countc = countc + 1
print(f"a soma de todos os valores foi: {soma} e o total de numeros foi: {countc}")
