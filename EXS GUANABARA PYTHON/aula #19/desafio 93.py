jogador = {}
somag = 0
gols = []
jogador['nome'] = str(input("NOME: "))
jogador['partidas'] = int(input("Quantas partidas jogou: "))
for i in range(jogador['partidas']):
    gol = (int(input(f"Jogo{i+1} GOLS: ")))
    gols.append(gol)
    somag = gol + somag 
jogador['total'] = somag
print(jogador, "GOLS: ", gols)
print("-===================-=-==-=-=--=--==-=-=-=-=-==---=-=-==--==")
for k, v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print(gols)
print("-=-=-=-=-==-==-==--=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-")
print(f"o jogador {jogador['nome']} jogou {jogador['partidas']} partidas")
for k, v in  enumerate(gols):
    print(f'jogo {k+1} fez {v} GOLS')
print(f'total de gols: {somag}')