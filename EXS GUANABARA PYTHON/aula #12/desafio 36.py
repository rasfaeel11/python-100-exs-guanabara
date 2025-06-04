valor = float(input("qual o valor da casa que voce quer comprar: "))
sal = float(input("qual o seu salario: "))
anos = int(input("e em quantos anos voce vai pagar: "))
meses = anos * 12
prest = valor / meses
prestmax = sal * 0.3
print(f"para pagar uma casa de R${valor} em {anos} anos a prestacao sera de R${prest:.2f}")
if prest > prestmax:
    print("emprestimo negado")
else:
    print("emprestimo aprovado")


