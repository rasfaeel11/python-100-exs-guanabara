expressao = str(input("digite uma expressao: "))
c = expressao.count("(")
c2 = expressao.count(")")
if c == c2:
    print("essa expressao e valida")
else:
    print("essa expressao e invalida")
