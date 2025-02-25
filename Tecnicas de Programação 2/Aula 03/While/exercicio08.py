print("Loja Luiz")
produto = 1
total = 0
i = 1
while produto !=0:
    produto = int(input(f"produto {i}:"))
    total += produto
    i +=1
print(f"Total: {total}")