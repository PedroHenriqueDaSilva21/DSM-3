votosBrancos = int(input("Digite a quantidade de votos em branco: "))
votosNulos = int(input("Digite a quantidade de votos nulos: "))
votosValidos = int(input("Digite a quantidade de votos Validos: "))

totalEleitores = votosBrancos + votosNulos + votosValidos

print(f"O percentual de votos brancos é de: {(votosBrancos * 100) / totalEleitores}")
print(f"O percentual de votos nulos é de: {(votosNulos * 100) / totalEleitores}")
print(f"O percentual de votos validos é de: {(votosValidos * 100) / totalEleitores}")

