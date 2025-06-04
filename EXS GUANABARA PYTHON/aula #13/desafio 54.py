countme = 0
countMA = 0
for c in range (0, 5):
    nasc = int(input("Em que ano a pessoa nasceu: "))
    if (2025 - nasc) > 18:
        countMA = countMA + 1
    else:
        countme = countme + 1
print(f"o total de pessoas maior de idade e: {countMA}")
print(f"o total de pessoas menor de idade e: {countme}")