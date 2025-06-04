km = float(input("de quantos kms vai ser a sua viagem: "))
if km <= 200:
    preço = km * 0.5
    print(f"voce vai pagar R${preço}")
else:
    preço = km * 0.45
    print(f"voce vai pagar R${preço}")
