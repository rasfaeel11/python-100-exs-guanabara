ano = int(input("digite o seu ano de nascimento: "))
idade = 2025 - ano
if idade <= 17 and idade >= 14:
    print("ATLETA JUVENIL")
elif idade >= 18:
    print("ATLETA SENIOR")
elif idade <= 13 and idade > 8:
    print("ATLETA INFANTIL")
elif idade > 3 and idade < 7:
    print("ATLETA MIRIM")