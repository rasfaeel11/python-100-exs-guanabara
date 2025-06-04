peso = float(input("digite o seu peso em KG: "))
altura = float(input("digite sua altura em M: "))
imc = peso / (altura * altura)
print(f"o seu IMC e de: {imc:.2f}")
if imc < 18.5:
    print("magreza")
elif imc > 18.5 and imc < 24.9:
    print("NORMAL")
elif imc > 25 and imc < 29.9:
    print("SOBREPESO")
elif imc > 30 and imc < 39.9:
    print("obesidade")
else:
    print("OBESIDADE GRAVE")