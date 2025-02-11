alturaParede = float(input("Digite a altura da parede: "))
larguraParede = float(input("Digite o valor da largura da parede: "))
alturaAzulejo = float(input("Digite a altura do azulejo: "))
larguraAzulejo = float(input("Digite a largura do azulejo: "))
areaParede = alturaParede * larguraParede
areaAzulejo = alturaAzulejo * larguraAzulejo

print(f"É necessário {areaParede / areaAzulejo} para azulejar a parede")
