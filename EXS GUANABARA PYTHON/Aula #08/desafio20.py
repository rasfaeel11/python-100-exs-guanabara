import random
nome1 = str(input("digite o nome do primeiro aluno: "))
nome2 = str(input("digite o nome do segundo aluno: "))
nome3 = str(input("digite o nome do terceiro aluno: "))
nome4 = str(input("digite o nome do quarto aluno: "))
nomeesc = [nome1, nome2, nome3, nome4]
random.shuffle(nomeesc)
print("o nome escolhido foi:")
print(nomeesc)