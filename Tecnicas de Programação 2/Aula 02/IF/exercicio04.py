num1 = int(print("Digite o primeiro numero"))
num2 = int(print("Digite o segundo numero"))

opcao = int(input("Digite a opção: "))

if opcao < 1 or opcao > 3:
    print("Opção inválida")
elif opcao == 1:
    media = (num1 * 2 + num2 * 3) / 5
    print(f"media ponderada calculada: {media}")
elif opcao == 2:
    quadrado = (num1 + num2) ** 2
    print(f"Quadrado da soma dos números: {quadrado} ")
else:
    if num1 < num2:
        cubo = num1 ** 3
        print(f"{num1} é o menor numero, ele elevado ao cubo é {cubo}")
    else:
        cubo = num2 ** 3
        print(f"{num2} é o maior número, ele elevado ao cubo é {cubo}")
