countidade = 0
counthomem = 0
countmulher = 0
while True:
    idade = int(input("digite a idade de quem voce quer cadastrar: "))
    sexo = str(input("digite o sexo de quem voce quer cadastrar: [M para mulher H para homem]: ")).strip().lower()[0]
    if sexo != "m" and sexo != "h":
        while sexo != "m" and sexo != "h":
            sexo = str(input("digite o sexo de quem voce quer cadastrar: [M para mulher H para homem]: ")).strip().lower()[0]
    if idade >= 18:
        countidade = countidade + 1
    if sexo == "h":
        counthomem = counthomem + 1
    if idade < 20 and sexo == "m":
        countmulher = countmulher + 1
    resp = str(input("Deseja continuar o cadastro? [S/N]: ")).strip().lower()[0]
    if resp == "n":
        break
print(f"a quantidade de pessoas maiores de idade sao {countidade}")
print(f"a quantidade de homens cadastrados sao {counthomem}")
print(f"a quantidade de mulheres abaixo de 20 anos cadastradas sao {countmulher}")