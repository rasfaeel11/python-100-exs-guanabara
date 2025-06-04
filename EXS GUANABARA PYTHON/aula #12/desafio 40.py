nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
media = (nota1 + nota2) / 2
print(f"a sua media foi de {media}")
if media >= 7:
    print("ALUNO APROVADO")
elif media >=4 and media < 7:
    print("ALUNO EM RECUPERACAO")
else:
    print("ALUNO REPROVADO")