soma = 0
cont = 0
for c in range(0, 6):
    num = int(input("digite um valor par qualquer para somar: "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f"o total de numeros pares foi: {soma} de {cont} numeros pares digitados")