lista1 = [10.0, "xx", True]
lista2 = [0, False, "xx"]
elemento_comum = False
for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_comum = True
if elemento_comum:
    print(f"As listas {lista1} e {lista2} possui elementos em comum")
else:
    print(f"As listas {lista1} e {lista2} NÃO possui elementos em comum")