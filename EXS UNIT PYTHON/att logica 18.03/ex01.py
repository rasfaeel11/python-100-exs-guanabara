print ("seja bem vindo a calculadora de despesas ")
salario = float(input("digite seu salario "))
agua = float(input("digite sua primeira conta de agua"))
energia = float(input("digite sua conta de energia "))
internet = float(input("digite sua conta de internet "))
alimentacao = float(input("digite sua conta de alimentacao "))
aluguel = float(input("digite sua conta de aluguel"))
restante = salario - agua - energia - internet - alimentacao - aluguel
gastos = agua + energia + internet + alimentacao + aluguel
print("seu montante restante e ", restante, "e seus gastos totais foram ", gastos)

#desafio
if restante < 0:
    print("voce esta negativado")
else:
    print("voce esta positivado ")
    