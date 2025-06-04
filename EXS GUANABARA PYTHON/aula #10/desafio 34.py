sal = float(input("digite seu salario: R$ "))
if sal > 1250:
    novosal = sal * 1.1
    print(f"o seu novo salario e de {novosal}")
else:
    novosal = sal * 1.15
    print(f"o seu novo salario e de {novosal}")