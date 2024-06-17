from pathlib import Path

# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário

caminho = Path.home()

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob("**/*"):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(arquivo)

encontra_arquivo(Path.cwd(), 'arquivo2')