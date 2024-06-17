from pathlib import Path
import shutil
import datetime

pasta_atual = Path(__file__).parent
pasta_a_organizar = pasta_atual / 'arquivos_desafio'
pasta_organizada = pasta_atual / 'organizada'
pasta_backups = pasta_atual / 'backups'

if pasta_organizada.exists():
    shutil.rmtree(pasta_organizada)

pasta_organizada.mkdir()

if not pasta_backups.exists():
    pasta_backups.mkdir()

for arquivo in pasta_a_organizar.glob("**/*"):
    if arquivo.is_file():
        pasta_organizada_c_ext = pasta_organizada / arquivo.suffix.replace(".", '')
        if not pasta_organizada_c_ext.exists():
            pasta_organizada_c_ext.mkdir()
        shutil.copy(arquivo, pasta_organizada_c_ext)

nome_backup = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(pasta_backups / nome_backup, 'zip', pasta_organizada)