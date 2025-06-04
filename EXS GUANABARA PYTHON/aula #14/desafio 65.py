resp = "S"
count = 0
s = 0
maior = 0
menor = 0
while resp != "N":
    num = int(input("digite um numero: "))
    resp = str(input("quer continuar: [S/N] ")).strip().upper()
    count = count + 1
    if count == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    s = s + num
    media = s / count
print(f"a quantidade de numeros digitados foi: {count} e media desses numeros foi {media}")
print(f"o maior numero fo {maior} e o menor numero foi {menor}")