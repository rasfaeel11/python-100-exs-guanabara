preco = 0.0
menor = 0.0
total = 0.0
count = 0
countpreco = 0
print ("-----------------------")
print("PAN RAFA DELICATESSEN")
print("-----------------------")
while True:
    produto = str(input("Nome do produto do cadastro: ")).lower().strip()
    preco = float(input("Preco: R$ "))
    total = total + preco
    if preco > 1000:
        countpreco = countpreco + 1
    count = count + 1
    if count == 1:
        barato = produto
        menor = preco
    if count >= 2 and menor > preco:
        barato = produto
        menor = preco
    resp = str(input("quer continuar? [s/n]: ")).lower().strip()[0]
    if resp == "n":
        break
print("========================================================")
print(f"o total da compra foi R${total}")
print(f"o total de produtos custando mais de r$1000 foi {countpreco}")
print(f"o produto mais barato foi {barato} que custa r${menor}")