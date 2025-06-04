print("SUPER GERADOR DE PA")
print("====================")
primeiro = int(input("digite o primeiro termo da pa: "))
razao = int(input("digite a razao da pa: "))
termo = primeiro
c = 0
while c < 10:
    c = c + 1
    print(termo)
    termo = termo + razao
maistermos = 1
totaltermos = 10
contadora = 0
while maistermos != 0:
    while maistermos > 0:
        maistermos = maistermos - 1
        print(termo)
        termo = termo + razao
    maistermos = int(input("quantos termos a mais voce quer ver: "))
    contadora = contadora + maistermos
totaltermos = totaltermos + contadora
print(f"FIM, o total de termos mostrados foi: {totaltermos}")