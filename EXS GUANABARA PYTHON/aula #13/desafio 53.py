frase = str(input("digite uma frase: ")).strip().replace(" ", "").lower
if frase == frase[::-1]:
    print("essa frase e um palindrimo")
else:
    print("essa frase nao e um palindromo")
