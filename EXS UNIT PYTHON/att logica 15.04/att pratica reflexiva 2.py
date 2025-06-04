print("Seja bem vindo a tela de Cadastro")
print("selecione a opcao na qual voce deseja prosseguir")
resp = int(input("[1] Cadastrar  [2] Sair"))
while resp != 2:
    if resp == 1:
        print("insira seus dados: ")
    else:
        print("opcao invalida")
    resp = (int(input("[1] para continuar [2] Sair")))

 
