valores = []
c = 0
while True:
    valores.append(int(input("digite um valor: ")))
    c = c + 1
    resp = str(input("quer continuar: [s/n]")).lower().strip()
    if resp == "n":
        break
print(f"voce digitou {c} elementos")
if 5 in valores:
    print("o numero 5 existe dentro da lista")
else:
    print("o numero 5 nao existe dentro da lista")
print(sorted(valores))