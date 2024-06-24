import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

data_json = '''
{
    "assinantes" : [
      {
        "nome": "Adriano Soares",
        "telefone": "51 99999999",
        "email": "adriano@email.com",
        "em_dia": true
      },
      {
        "nome": "Juliano faccioni",
        "telefone": "51 99999999",
        "email": "juliano@email.com",
        "em_dia": false
      }
      ],
    "data_extração": "2023/08/22"
}
'''

# Convertendo json para dicionário
dado_convertido = json.loads(data_json)
'''
print(type(data_json))
print(type(dado_convertido))
print(dado_convertido)


# Convertendo novamente para json
dado_desconvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
print(type(dado_convertido))
print(type(dado_desconvertido))
print(dado_desconvertido)

# Lendo arquivos json
'''

pasta_atual = Path(__file__).parent
with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
    dado_carregado = json.load(f)
'''
    print(type(dado_carregado))
    print(dado_carregado)
    print(dado_carregado['assinantes'])
'''

# Escrevendo arquivos json
with open(pasta_atual / 'jsons' / 'assinantes_copia.json','w') as f:
    json.dump(dado_carregado, f, ensure_ascii=False, indent=2)