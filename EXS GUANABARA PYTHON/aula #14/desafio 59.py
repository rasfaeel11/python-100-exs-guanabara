num1 = int(input("Primeio valor: "))
num2 = int(input("Segundo valor: "))
print("=========OPÇÕES==========")
print("[1] SOMAR")
print("[2] MULTIPLICAR")
print("[3] MAIOR")
print("[4] NOVOS NUMEROS")
print("[5] SAIR")
opcao = 0
while opcao != 5:
    opcao = int(input("qual a sua opcao? "))
    match opcao:
        case 1:
            print(num1 + num2)
        case 2:
            print(num1 * num2)
        case 3:
            if num1 > num2:
                print(f"o maior numer entre {num1} e {num2} e: {num1}")
            else:
                print(f"o maior numer entre {num1} e {num2} e: {num2}")
        case 4:
            num1 = int(input("Primeiro valor: "))
            num2 = int(input("Segundo valor: "))
        case 5:
            print("finalizando...")
    if opcao > 5:
        print("opcao invalida...")
        opcao = int(input("tente novamente: "))
print("Programa encerrado!")
            