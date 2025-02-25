numero = int(input("Digite o numero que deseja saber a tabuada: "))
inicio = int(input("Digite daonde começar a tabuada: "))
fim = int(input("Digite daonde finalizar a tabuada: "))

while inicio <= fim:
    print(f"{numero} * {inicio} = {numero * inicio}")
    inicio += 1