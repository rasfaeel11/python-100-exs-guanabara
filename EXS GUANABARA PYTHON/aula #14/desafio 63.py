print("SEQUENCIA DE FIBONACCI")
print("========================")
termos = int(input("quantos termos voce quer mostrar: "))
c = 0
t1 = 0
t2 = 1
t3 = t1 + t2
while  c < termos:
    print(t3)
    c = c + 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    
    