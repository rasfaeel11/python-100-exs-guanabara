# escola = []
# nomes = {}
# nomes['nome'] = str(input("NOME: "))
# nomes['media'] = float(input("MEDIA: "))
# escola.append(nomes)

# for s in escola:
#     for k, v in s.items():
#         print(f'{k} é {v}')
# if nomes['media'] >= 7:
#     print('SITUAÇÃO: APROVADO')
# elif nomes['media'] > 4.1 and nomes['media'] < 6.9:
#     print('SITUAÇÃO: RECUPERAÇÃO')
# else:
#     print('SITUAÇÃO: REPROVADO')

aluno = {}
aluno['nome'] = str(input("NOME: "))
aluno['media'] = float(input(F"media do {aluno['nome']}"))
if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] > 4 and aluno['media'] < 7:
    aluno['situação'] = 'recuperacao'
else:
    aluno['situação'] = 'reprovado'
for i, j in aluno.items():
    print(f'{i} é {j}')