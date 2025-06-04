def area(comp, larg):
    res = comp * larg
    print(f' a largura é {larg} e o comprimento e {comp} e a area total é {res}')

l = float(input("digite a largura do sua area: "))
c = float(input("digite o comprimento de sua area: "))
area(c, l)