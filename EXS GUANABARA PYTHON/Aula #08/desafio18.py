import math
num = float(input("digite um angulo qualquer: "))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
seno = math.sin(math.radians(num))
print("o coseno e {:.2f} a tangente e {:.2f} e o seno e {:.2f} ".format(coseno, tangente, seno))