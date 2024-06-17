seq = [1, 2, 3, 4, 5, 6]
soma = 0

for x in seq:
    soma += x
    print(f"Foi somado {x} e agora o valor vale {soma}")
media = soma/len(seq)
print(len(seq))
print(f"Média {media}, Soma {soma}")
