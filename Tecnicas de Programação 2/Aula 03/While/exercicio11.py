nomes = ["Luiz","Ana","Cristina","Fernanda","Maria","Joaquina"]
sair = 1
while sair != 0:
    localizar = input("Digite o nome a ser procurado: ")

    for nome in nomes:
        if nome == localizar:
            print(f"O nome {localizar} foi encontrado")
            break
        else:
            print("O nome não foi localizado")
    sair = int(input("Digite 1 - Buscar, 0 - Sair"))