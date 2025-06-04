# aluguel de carros
dias = int(input("quantos dias voce ficou com o carro: "))
kms = int(input("quantos kms voce ficou com o carro: "))
pagamentodias = 60 * dias
pagamentoskms = 0.15 * kms
pagamentot = pagamentodias + pagamentoskms
print("o total a pagar e {}".format(pagamentot))