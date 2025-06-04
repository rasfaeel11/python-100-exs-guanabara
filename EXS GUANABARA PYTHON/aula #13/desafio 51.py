print("===================")
print("10 TERMOS DE UMA PA")
print("===================")
inicio = int(input("digite o primeiro termo: "))
razao = int(input("digite sua razao: "))
decimo = inicio + (11 - 1) * razao
for c in range(inicio, decimo, razao):
    print(c)