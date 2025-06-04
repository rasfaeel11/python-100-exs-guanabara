num = 0
count = 0
res = 0
while num != 999:
    num = int(input("digite um numero para somar: "))
    res = res + num
    count = count + 1
res = res - 999
count = count - 1
print(f"a soma dos numeros foi {res} e o total de numeros digitados foi: {count}")
print(res)