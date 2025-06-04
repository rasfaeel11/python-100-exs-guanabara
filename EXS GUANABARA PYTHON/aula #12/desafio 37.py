num = int(input("digite um numero qualquer: "))
escolha = int(input("digite [1] para BINARIO, [2] para OCTAL, [3] para HEXADECIMAL: "))
if escolha == 1:
    print(f"{num} em sistemas binarios é: {bin(num)[2:]}")
elif escolha == 2:
    print(f"{num} em sistemas OCTAL é: {oct(num)[2:]}")
elif escolha == 3:
    print(f"{num} em sistemas HEXA é: {hex(num)[2:]}")
else:
    print("opcao invalida")