dados = {}
dados['nome'] = 'rafael'
dados['sexo'] = 'M'
dados['idade'] = 19
print(dados)
del dados['sexo']
filme = {'filme': 'Vingadores',
         'ano': 2012,
         'diretor': 'joss whedon'}
print(filme)
for k, v in filme.items():  #k = key, v = value
    print(f"o {k} e {v}")   
#listas com dicionarios embutidos
brasil = []
estado1 = {'uf': 'PE', 'nome': 'PERNAMBUCO'}
estado2 = {'uf': 'SP', 'nome': 'SAO PAULO'}
brasil.append(estado1)
brasil.append(estado2)

estado = []
brasil = {}
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla: "))
