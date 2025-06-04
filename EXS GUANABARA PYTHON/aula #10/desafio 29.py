vel = float(input("qual foi a velocidade do seu carro? "))
if vel > 80:
    vel2 = vel - 80
    vel2 = 7 * vel2
    print(f"voce ultrapassou o limite e vai ter que pagar R${vel2} de multa!")
else:
    print("voce esta dentro do limite!")