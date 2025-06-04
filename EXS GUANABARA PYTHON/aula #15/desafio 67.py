tab = 0
rtab = 0
c = 0
while True:
    tab = int(input("quer ver a tabuada de qual valor: "))
    c = 0
    if tab < 0:
        break
    while c < 10:
        c = c + 1
        rtab = tab * c
        print(f"{tab} x {c} = {rtab}")
print("PROGRAMA ENCERRADO.")