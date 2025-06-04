ano = int(input("em que ano voces nasceu: "))
anoatual = 2025
idade = anoatual - ano
print(f"quem nasceu em {ano} tem {idade} anos")
if idade < 18:
    idade2 = 18 - idade
    print(f"ainda faltam {idade2} anos para o alistamento.")
    anoalist = idade2 + anoatual
    print(f"seu alistamento sera no ano de: {anoalist} ")
elif idade > 18:
    idade2 = idade - 18
    print(f"voce ja deveria ter se alistado a: {idade2} anos ")
    anoalist = ano + 18
    print(f"seu alistamento foi em {anoalist}")
else:
    print("voce ja pode se alistar!")