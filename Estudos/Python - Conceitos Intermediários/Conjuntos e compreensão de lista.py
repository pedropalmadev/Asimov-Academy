# NOVA_LISTA = [RESULTADO para cada ELEMENTO em SEQUÊNCIA se CONDIÇÃO]
'''

NOVA_LISTA = []
para cada ELEMENTO em SEQUÊNCIA:
  se CONDIÇÃO:
      RESULTADO entra em NOVA_LISTA

'''

# desafio 01
# converta o loop abaixo para uma compreensão de lista:
'''
valores = [30, 50, 100, 120]
triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)

print(triplos)

triplos = [valor*3 for valor in valores]
print(triplos)


# desafio 02
palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']


dict_caracteres = {palavra.lower() : len(palavra.replace(" ","")) for palavra in palavras}

print(dict_caracteres)


# Desafio 03
gosta_programar = {"Ricardo", "Roberto", "Pedro", "Vinicius"}
gosta_futebol = {"Mateus", "Roberto", "Paulo", "Vinicius"}
estuda_asimov = {"Ricardo", "Mateus", "Paulo", "Pedro"}

R = gosta_programar.intersection(estuda_asimov).difference(gosta_futebol)
print(R)
'''