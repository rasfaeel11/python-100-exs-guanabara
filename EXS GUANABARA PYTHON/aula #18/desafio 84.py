lista = []
peso = []
maior = 0
menor = 0
pessoamenor = "x"
pessoamaior = "x"
c = 0
while True:
    lista.append(str(input("NOME: ")))
    peso.append(float(input("PESO: ")))
    if c == 0:
        maior = menor = peso[0]
    else:
        if peso[0] > maior:
            maior = peso[0]
            pessoamaior = lista[0]
        if peso[0] < menor:
            menor = peso[0]
            pessoamenor = lista[0]
    c = c + 1
    resp = str(input("CONTINUAR: [S/N]")).upper().strip()
    peso.clear()
    lista.clear()
    if resp == "N":
        break
print(f"CADASTRO TOTAL DE {c} PESSOAS")
print(f"MAIOR PESO KGS {maior} de {pessoamaior} ")
print(f"MENOR PESO DE {menor} de {pessoamenor} ")
print(lista)