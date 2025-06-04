par = []
impar = []
while True:
    n = int(input("digite um valor: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input("quer continuar: [s/n] ")).lower().strip()
    if resp == "n":
        break
total = par + impar
print(par)
print(impar)
print(total)