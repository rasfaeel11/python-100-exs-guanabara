n = 0
count = 0
s = 0
while True:
    n = int(input("digite um numero para realizar a soma: "))
    if n == 999:
        break
    s = s + n
    count = count + 1
print(f"o total de numeros digitados foi {count} e a soma deles foi {s}")