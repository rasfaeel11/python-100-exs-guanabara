valores = []
while True:
    valores.append(int(input("digite um valor para ser adicionado: ")))
    resp = str(input("quer continuar [s/n]")).lower().strip()
    if resp == "n":
        break
print("os valores digitados foram: ", sorted(valores))