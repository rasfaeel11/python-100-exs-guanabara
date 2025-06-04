seg1 = int(input("digite o primeiro segmento do triangulo: "))
seg2 = int(input("digite o segundo segmento do triangulo: "))
seg3 = int(input("digite o terceiro segmento do triangulo: "))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    if seg1 == seg2 == seg3:
        print("OS SEGMENTOS FORMAM UM TRIANGULO EQUILATERO")
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print("OS SEGMENTOS FORMAM UM ISOSCELES")
    elif seg1 != seg2 and seg2 != seg3:
        print("OS SEGMENTOS FORAM UM TRIANGULO ESCALENO")
else:
    print("NAO E UM TRIANGULO")