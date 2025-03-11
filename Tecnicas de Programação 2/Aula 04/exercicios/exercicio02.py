matriz_numeros = []
for i in range(0,4):
    linha = []
    matriz_numeros.append(linha)
    for j in range(0,4):
        numero = float(input(f"Digite o número para a posição ({i},{j}): "))
        linha.append(numero)

for i in range (0,4):
    print(matriz_numeros[i])