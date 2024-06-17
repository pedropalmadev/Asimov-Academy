from pathlib import Path

# Lendo um arquivo forma nao recomendada
'''
pasta_atual = Path(__file__).parent

lista_compras = open(pasta_atual / 'lista_de_compras.txt')

print(lista_compras.read())

lista_compras.close()

# Lendo arquivos forma recomendada
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt', mode='r') as lista_compras:
    print(lista_compras.read())

# Lendo linha a linha
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt', mode='r') as lista_compras:
    linha = lista_compras.readline()
    while linha != "":
        print(linha, end='')
        linha = lista_compras.readline()

# Lendo todas as linhas
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    print(lista_compras.readlines())


# Escrevendo arquivo
pasta_atual = Path(__file__).parent
items_ja_comprados = ['farinha','fermento','agua','mel','mamao']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        print(item)
        if not item.replace("\n",'') in items_ja_comprados:
            lista_atualizada.write(item)


# Escrevendo linha a linha
pasta_atual = Path(__file__).parent
items_ja_comprados = ['farinha','fermento','agua','mel','mamao']

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:
    if not item.replace("\n", '') in items_ja_comprados:
        itens_lista_atualizada.append(item)
print(itens_lista)
print(itens_lista_atualizada)
with open('lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n','')
    lista_atualizada.writelines(itens_lista_atualizada)
'''
# Acrescentando valores a um arquivo

pasta_atual = Path(__file__).parent

novos_itens = ['banana']

novos_itens_c_quebra = []
for item in novos_itens:
    novos_itens_c_quebra.append(f'\n{item}')
with open('lista_de_compras.txt',mode='a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens_c_quebra)