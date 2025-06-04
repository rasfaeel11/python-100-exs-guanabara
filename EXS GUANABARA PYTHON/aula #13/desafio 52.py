num = int(input("digite um numero: "))
count = 0
for c in range(1, num+1):
    if num % c == 0 and num % num == 0:
        print(f"{num} e diviso por: {c}")
        count = count + 1
if count <= 2:
    print("e por isso e numero primo")
else:
    print("e por isso nao e um numero primo")