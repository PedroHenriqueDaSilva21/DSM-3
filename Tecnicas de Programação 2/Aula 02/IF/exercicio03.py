estatura1 = float(input("Digite a estatura da pessoa 1: "))
estatura2 = float(input("Digite a estatura da pessoa 2: "))
estatura3 = float(input("Digite a estatura da pessoa 3: "))


if estatura1 > estatura2 and estatura2 > estatura3:
    print(f"{estatura1},{estatura2},{estatura3}")
elif estatura1 < estatura2 and estatura2 < estatura3:
    print(f"{estatura3},{estatura2},{estatura1}")
elif estatura1 > estatura2 and estatura1 < estatura3:
    print(f"{estatura3},{estatura1},{estatura2}")
else:
    print(f"{estatura2},{estatura1},{estatura3}")
