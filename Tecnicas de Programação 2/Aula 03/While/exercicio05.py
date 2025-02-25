contador = 1
votosA  = 0
votosC = 0
votosD = 0
while contador <= 4:
    votacao = input("Vote em A, C ou D: ")
    match(votacao.upper()):
        case "A":
            votosA += 1
        case "C":
            votosC += 1
        case "D":
            votosD += 1
        case _:
            print("Voto Inválido, não computado")
    contador+=1

print(f"Votos A: {votosA}")
print(f"Votos C: {votosC}")
print(f"Votos D: {votosD}")

        

    