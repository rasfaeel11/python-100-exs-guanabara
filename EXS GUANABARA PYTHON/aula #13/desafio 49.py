tab = int(input("digite um numero para ver sua tabuada: "))
resultado = 0
for c in range(0, 11):
    resultado = tab * c
    print(f"{tab} x {c} = {resultado}" )