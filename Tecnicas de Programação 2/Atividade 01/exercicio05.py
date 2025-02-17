custoFabrica = float(input("Leia o valor de custo de fábrica do carro: "))

custoFabrica +=  custoFabrica * 0.28 # Distribuidor
custoFabrica += custoFabrica * 0.45 # Impostos

print(f"O custo para o consumidor é de: {custoFabrica}")