idadevelha = 0
countmuie = 0
media = 0
for c in range (1, 5):
    print(f"======PESSOA {c}=======")
    nome = str(input("NOME: ")).strip().lower()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().lower()
    media = media + idade
    if sexo == "f" and idade < 20:
        countmuie = countmuie + 1
    if nome and idade and sexo == 1:
        genvelho = sexo
        nomevelho = nome
        idadevelha = idade
    else:
        if idadevelha < idade:
            idadevelha = idade
            nomevelho = nome
            genvelho = sexo
media = media / 4
print(f"A pessoa mais velha é {nomevelho} e ele em {idadevelha} anos")
print(f"ao todo sao mulheres {countmuie} com menos de 20 anos")
print(f'a media de idade do seu grupo e {media}')
    