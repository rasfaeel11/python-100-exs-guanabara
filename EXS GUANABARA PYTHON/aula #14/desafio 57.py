sexo = str(input("qual o seu sexo: [M/F] ")).upper()
if sexo != "M" and sexo != "F":
    while sexo != "M" and sexo != "F":
        sexo = str(input("dados invalidos, por favor digite novamente o seu sexo: ")).upper()
print('dados corretos! podem prosseguir')