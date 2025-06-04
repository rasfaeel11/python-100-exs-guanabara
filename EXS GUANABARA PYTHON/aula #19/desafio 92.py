dados = {}
dados['nome'] = str(input("NOME: "))
dados['nascimento'] = int(input("DATA NASCIMENTO: "))
dados['clt'] = int(input("CLT[0] para caso nao possua: "))
if dados['clt'] == 0:
    for k, v in dados.items():
        print('=-=-=-=-===-=--=-=-==--=-=-==-=--=-=')
        print(f'{k} tem o valor {v}')
else:
    dados['anocontratacao'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('SALARIO: R$'))
    dados['aposentadoria'] = dados['anocontratacao'] + 35
    print('-=-=--==-=-==-=-=--=-=-==--=-==-=--==---===-=--=')
    for k, v in dados.items():
        print(f'{k} tem o valor de {v}')