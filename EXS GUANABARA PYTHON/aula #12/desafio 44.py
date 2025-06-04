print("LOJA RAFAES")
print("==============")
compras = float(input("PREÇO DAS COMPRAS: R$ "))
print("[1] para a vista no dinheiro ")
print("[2] para a vista no cartao")
print("[3] para 2x no cartao")
print("[4] para 3x ou mais no cartao")
opcao = int(input("qual e a opcao: "))
if opcao == 1:
    desc = compras * 0.10
    comprasnvalor = compras - desc
    print(f"o seu total de compras ficou {compras} mas com o desconto ficou {comprasnvalor}")
elif opcao == 2:
    desc = compras * 0.05
    comprasnvalor = compras - desc
    print(f"o total de suas compras ficou {compras} mas com o desconto ficou {comprasnvalor}")
elif opcao == 3:
    print(f"o valor total de suas compras foi {compras}")
elif opcao == 4:
    parcelas = int(input("em quantas parcelas voce deseja? "))
    desc = compras * 0.20
    comprasnvalor = compras + desc
    valparcelas = comprasnvalor / parcelas
    print(f"o total de suas compras foi {compras} mas com juros ficou {comprasnvalor} no total de {parcelas} parcelas de R${valparcelas}")