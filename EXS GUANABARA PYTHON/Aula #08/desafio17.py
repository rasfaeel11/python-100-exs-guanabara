import math
cateto_oposto = float(input("digite o cateto oposto: "))
cateto_adj = float(input("digite o cateto adjacente: "))
comp_hipotenusa = math.sqrt(cateto_oposto * cateto_oposto + cateto_adj * cateto_adj)
print(comp_hipotenusa)