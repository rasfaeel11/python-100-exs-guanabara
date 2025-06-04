matriz = [[], [], []]
maior = 0
par = []
somac = 0
for l in range(0, 3): # CRIA AS LINHAS DA MATRIZ
    for c in range(0, 3): # CRIAS AS COLUNAS DA MATRIZ
        valor = int(input(f'digite o valor de {l}.{c}: '))
        if valor % 2 == 0:
            par.append(valor)
        matriz[l].append(valor)
        if valor > maior: #MAIOR VALOR DA MATRIZ, INDEPENTEDETE
            maior = valor
        if c == 2: #PEGA A 3 COLUNA POR CONTA DO C(COLLUNA)
            somac = somac + valor
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end="")
    print()
print(f"valores pares: {par}")
print(f"o maior valor e {maior}")
print(f"a soma da terceira coluna e {somac}")