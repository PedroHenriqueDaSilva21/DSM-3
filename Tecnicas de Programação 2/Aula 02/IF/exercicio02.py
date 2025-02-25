numero = int(input("Digite um valor: "))

categoriaNumero = numero % 2

if categoriaNumero == 0:
    calculo = pow(numero,2)
    print(f"O numero é par e seu quadrado é de: {calculo}")
else:
    calculo = pow(numero,3)
    print(f"O numero é impar e seu cubo é de: {calculo}")