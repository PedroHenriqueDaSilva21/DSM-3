valorPrestacao = float(input("Digite o valor da prestação: "))
taxaJuros = float(input("Digite a taxa de juros: "))
quantidadeMeses = int(input("Digite a quantidade de meses em atraso: "))

valorAtraso = valorPrestacao + (valorPrestacao * (taxaJuros/100) * quantidadeMeses)

print(f"A quantidade de de valor a ser pago em atraso é de: {valorAtraso}")