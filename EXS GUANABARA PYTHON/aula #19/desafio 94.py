dados = {}
mulheres = []
acimamedia = []
idadeacima = []
c = 0
media = 0
soma = 0
while True:
    c = c + 1
    dados['nome'] = str(input("NOME: "))
    dados['sexo'] = str(input("SEXO[M/F]: ")).upper()
    if dados['sexo'] == "F":
        mulheres.append(dados["nome"])
    dados['idade'] = int(input("IDADE: "))
    soma = soma + dados['idade']
    resp = str(input("CONTINUAR[S/N]: ")).lower().strip()
    if resp == "n":
        break
media = soma / c
for i in range(dados['idade']):
    if i > media:
        acimamedia.append(dados['nome'])
        idadeacima.append(dados['idade'])
print(f"ao todos temos {c} cadastros")
print(f"a media de idade e {media}")
print(f"as mulheres cadastradas foram {mulheres}")
print(f"lista de pessoa que estao acima da media: {acimamedia}")
