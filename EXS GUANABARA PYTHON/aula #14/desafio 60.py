fatorial = int(input("digite o valor para calcular uma fatorial: "))
fatorialo = fatorial
res = 1
while fatorial > 0:
    res = fatorial * res
    fatorial = fatorial - 1
    print(f"{res} x {fatorial}")
print(f"a fatorial de {fatorialo} é: {res}")