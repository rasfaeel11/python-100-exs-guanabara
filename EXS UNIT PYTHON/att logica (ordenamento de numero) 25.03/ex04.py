# Rafael Melo, Pedro Florencio e William Santos
# 25.03
a = 1
b = int(input("insira um número:"))
c = int(input("insira outro número:"))

if a > b and a > c and b > c:
    print("Em ordem decrescente:", a, b, c)
if a > c and a > b and c > b:
     print("Em ordem decrescente:", a, c, b)
if b > a and b > c and a > c:
    print("Em ordem decrescente:", b, a, c )
if b > a and b > c and c > a:
    print ("Em ordem decrescente:", b, c, a )
if c > a and c > b and a > b:
    print("Em ordem decrescente:", c, a, b)
if c > a and c > b and b > a:
    print("Em ordem decrescente:", c, b, a)
if c == a and c == b and b == c:
    print("os tres numeros sao iguais")
if a > b and c == b:
    print (a, c, b, "dois numeros iguais")
if b > a and a == c:
    print (b, c, a, "dois numeros iguais")
if c > a and a == b:
    print(c, b, a, "dois numeros iguais")