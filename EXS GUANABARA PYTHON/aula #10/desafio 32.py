ano = int(input("em que anos nos estamos? ")) # o usuario digita o ano
if ano % 4 == 0: # comeca uma condicional, se ele for divisivel por 4, entao vai executar outro bloco
    if ano % 100 == 0 and ano % 400 != 0: # se ele for tambem divisel por 100 e nao for divisivel por  400, executa o print
        print('voce nao esta num ano bissexto')
    else:                                # se ele for divisivel pelos dois, ele e bissexto!
        print("voce  esta num ano bissexto!")
else:
    print("voce nao esta num ano bissexto !")