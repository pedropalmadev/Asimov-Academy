import random
import string
from pathlib import Path


pasta_atual = Path(__file__).parent
formatos_de_arquivos = ['.py', '.pdf', '.txt', '.csv', '.xlsx', '.json', '.html']


def arquivo_randomico(quantidade):

    letters = string.ascii_lowercase
    arquivos = [''.join(random.choice(letters) for i in range(random.randint(4, 8))) for _ in range(quantidade)]
    arquivos = [f'{nome}{formatos_de_arquivos[random.randint(0, len(formatos_de_arquivos) - 1)]}' for nome in arquivos]
    return arquivos


for arquivo in arquivo_randomico(50):
    with open(pasta_atual / 'arquivos_desafios' / arquivo, 'w') as f:
        f.write(arquivo)
