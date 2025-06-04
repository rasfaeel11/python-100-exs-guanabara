sorteio = (int(input("digite um valor: ")),
           int(input("digite mais um valor: ")),
           int(input("digite um valor: ")),
           int(input("digite um valor: ")),
           int(input("digite um valor: ")))
cpar = 0
print(sorteio)
print(sorteio.count(9))
if sorteio.count(3) >= 1:
    print("a posicao do numero 3  foi: ", sorteio.index(3) + 1)
else:
    print("nao tem nenhum numero 3")
for i in sorteio:
    if i % 2 == 0:
        cpar = cpar + 1
print(cpar)