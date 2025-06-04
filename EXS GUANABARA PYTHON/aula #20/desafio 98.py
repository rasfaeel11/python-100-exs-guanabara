def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        while inicio >= fim:
            print(inicio, ' ', end='')
            inicio = inicio - passo
        print('-'*30)       
    if inicio < fim:
        while fim >= inicio:
            print(inicio, ' ', end='')
            inicio = inicio + passo
        print('-'*30)
contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez ')
a = int(input("digite um valor para inicio: "))
b = int(input("digite um valor para o fim: "))
c = int(input("digite um valor para o passo: "))
contador(a, b, c)