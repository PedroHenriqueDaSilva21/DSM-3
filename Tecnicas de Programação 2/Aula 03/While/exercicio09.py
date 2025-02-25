nomes = ["Maria","João","Paulo","Magali"]
localizar = input("Digite o nome a ser procurado: ")

for nome in nomes:
    if nome == localizar:
        print(f"O nome {localizar} foi encotrado")
        break
    else:
        print("O nome não foi localizado")