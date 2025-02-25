indice = int(input("Digite o indice de poluição: "))

match(indice):
    case 0|  1 | 2:
        print("Aceitável")
    case 3 | 4 | 5:
        print("Suspendar Atividades Grupo I")
    case 6 | 7:
        print("Suspender Atividades Grupo I e II")
    case _:
        print("Suspender todos os grupos")