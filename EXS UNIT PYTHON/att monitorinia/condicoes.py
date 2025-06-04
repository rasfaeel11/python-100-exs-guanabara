# notas = []
# soma = media = 0
# for i in range(1, 5):
#     notas.append(float(input(f"NOTA {i}: ")))
# for i in notas:
#     soma = soma + i
# media = soma / 4
# print(media)
# num = []
# par = []
# impar = []
# for i in range(1, 5):
#     num.append(int(input(f"NUMERO {i}: ")))
#     if i % 2 == 0:
#         par.append(i)
#     else:
#         impar.append(i)
# print(par)
# print(impar)
# nomes = ['carlos', 'bolsonaro', 'lula', 'cassandra']
# countc = 0
# for i in nomes:
#     if i[0] == "c":
#         countc = countc + 1
# print(countc)
# num = []
# for i in range(1,5):
#     num.append(int(input(f"NUMERO {i}: ")))
# numb = int(input("BUSCA: "))
# encontrado = False
# for i, j in enumerate(num):
#     if j == numb:
#         print(f"foi encontrado na poscao {i}")
#         encontrado = True
# if not encontrado:
#     print("valor nao existente")
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        valores = int(input(f"digite um valor {l}.{c}: "))
        matriz[l].append(valores)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()