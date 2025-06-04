n1 = int(input("digite um numero qualquer: "))
n2 = int(input("digite outro numero: "))
n3 = int(input("digit apenas mais um: "))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f"o maior numero e {n1}")
    print(f"o menor numero e {n3}")
if n2 > n1 and n2 > n3 and n1 > n3:
    print(f"o maior numero e {n2}")
    print(f"o menor numero e {n3}")
if n3 > n1 and n3 > n2 and n2 > n1:
    print(f"o maior numero e {n3}")
    print(f"o menor numero e {n1}")
if n3 > n1 and n3 > n2 and n1 > n2:
    print(f"o maior numero e {n3}")
    print(f"o menor numero e {n2}")
if n2 > n1 and n2 > n3 and n3 > n1:
    print(f"o maior numero e {n2}")
    print(f"o menor numero e {n1}")
if n1 == n2 and n2 == n3:
    print("numeros iguais!")