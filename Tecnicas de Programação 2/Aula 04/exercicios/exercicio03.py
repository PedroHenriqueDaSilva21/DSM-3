matriz_numeros = []
for i in range(0,2):
    linha = []
    matriz_numeros.append(linha)
    for j in range(0,3):
        numero = input(f"Digite a Capital para a posição ({i},{j}): ")
        linha.append(numero)

for i in range (0,2):
    print(matriz_numeros[i])