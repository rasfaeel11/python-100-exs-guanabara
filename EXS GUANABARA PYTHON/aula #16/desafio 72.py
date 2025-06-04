extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
escolha = int(input("digite um valor de 0 a 10: "))
for i in extenso:
    if escolha > 10:
        escolha = int(input("valor incorreto, tente novamente: "))
    elif escolha < 0:
        escolha = int(input("valor incorreto, tente novamente: "))
    else:
        print(extenso[escolha])
        break
print("acabou!")