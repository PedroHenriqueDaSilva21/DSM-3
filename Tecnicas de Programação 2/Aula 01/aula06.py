salario = float(input("Digite o salário total do usuário: "))
percentual = float(input("Digite o percentual de incremento: "))

novoSalario = salario + (salario * (percentual / 100))

print(f"O reajuste do salário é de {novoSalario}")