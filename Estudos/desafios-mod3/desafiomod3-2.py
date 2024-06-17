seq = [1, 3, 43, 5, 7, 12]
maior = 0
for x,y in enumerate(seq):
    seq[0] = maior
    if seq[x] > maior:
        maior = seq[x]
    print(x,y)
print(maior)