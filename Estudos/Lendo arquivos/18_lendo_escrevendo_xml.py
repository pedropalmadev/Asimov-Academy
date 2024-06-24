import xml.dom.minidom
from pathlib import Path

# Lendo arquivos xml
pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse(str(pasta_atual / 'xmls' / 'livros.xml'))

group = domtree.documentElement
livros = group.getElementsByTagName('livro')


# Interando por elementos e retornando valores
for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue

    print(f'Titulo: {titulo} <--> Autor: {autor}')


# Salvando um arquivo xml
livros[0].getElementsByTagName('autor')[0].childNodes[0].nodeValue = 'Abreu, Pedro'

with open(pasta_atual / 'xmls' / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)

