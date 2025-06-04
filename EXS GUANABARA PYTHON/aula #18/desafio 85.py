tot = [[], []]
for i in range(0, 4):
    n = int(input("digite um numero: "))
    if n % 2 == 0:
        tot[0].append(n)
    else:
        tot[1].append(n)
print(tot[0])
print(tot[1])