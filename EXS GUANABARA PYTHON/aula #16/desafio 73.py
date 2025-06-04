times_brasileirao_2025 = ("Flamengo", "Palmeiras", "Red Bull Bragantino", "Cruzeiro", "Fluminense",
                           "Internacional", "Bahia", "Botafogo", "Ceará", "São Paulo", "Vasco", "Corinthians",
                             "Juventude", "Mirassol", "Fortaleza", "Vitória", "Atlético-MG", "Grêmio", "Santos", "Sport")
top4 = (times_brasileirao_2025[0: 4])
rebaixados = (times_brasileirao_2025[16: 20])
pos = (times_brasileirao_2025.index("Palmeiras"))
print(f"TOP 4: {top4} ")
print("==========================================================================================")
print(f"REBAIXADOS : {rebaixados}")
print("==========================================================================================")
print("Ordem alfabetica: ", sorted(times_brasileirao_2025))
print("==========================================================================================")
print("o palmeiras esta na posicao: ", pos + 1)
print("==========================================================================================")