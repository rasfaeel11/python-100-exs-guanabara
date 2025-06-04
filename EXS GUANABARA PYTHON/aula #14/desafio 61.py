print("GERADOR DE PA")
print("==============")
pt = int(input("digite o primeiro termo da pa: "))
razao = int(input("digite a razao da sua PA: "))
c = 0
while c < 10:
    c = c + 1
    pa = pt + (c - 1) * razao
    print(pa)
