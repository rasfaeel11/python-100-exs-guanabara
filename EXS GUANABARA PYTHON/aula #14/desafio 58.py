from random import randint
print("sou seu computador pai, voce nao ganha de mim nem fudendo. Pensei num numero, tenta adivinha ai.")
numc = randint(0, 10)
numu = int(input("digite sua resposta: "))
counte = 0
while numu != numc:
    if numu > numc:
        numu = int(input("poxa, voce errou. tente denovo (uma dica, esta pra baixo do numero escolhido): "))
    if numu < numc:
        numu = int(input("poxa, voce errou. tente denovo (uma dica, esta pra cima do numero escolhido):  "))
    counte = counte + 1
print(f"caramba, voce acertou!, o numer que escolhi foi {numc} e so demorou {counte} tentativas")