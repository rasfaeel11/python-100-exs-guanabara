matriz = [[],[],[]]
pares = 0
somacoluna = 0
maiorvalor = 0
for l in range(0,3):
        for c in range(0,3):
                valor = int(input(f"digite um valor para  [{l}.{c}]"))
                if valor % 2 == 0:
                        pares = pares + valor
                if c == 1:
                        somacoluna = somacoluna + valor
                matriz[l].append(valor)
                if valor > maiorvalor:
                        maiorvalor = valor
                
print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print(f"a soma de pares e {pares}")
print(f"a soma da 3 coluna e {somacoluna}")
print(f"o maior valor da segunda coluna e {maiorvalor}")

