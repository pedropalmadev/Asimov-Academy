from pathlib import Path
import pandas as pd
# Resolução do aluno (em baixo resolução do professor)
pasta_atual = Path(__file__).parent
'''
# Lendo as tabelas de cada aba
tabela_clientes_rs = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RS')
tabela_clientes_sc = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC')
tabela_clientes_pr = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='PR')
tabela_clientes_sp = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SP')

# Escrevendo/Importando as tabelas para o excel
tabela_clientes_rs.to_excel(pasta_atual / 'planilhas_separadas' / 'RS.xlsx', index=False)
tabela_clientes_sc.to_excel(pasta_atual / 'planilhas_separadas' / 'SC.xlsx', index=False)
tabela_clientes_pr.to_excel(pasta_atual / 'planilhas_separadas' / 'PR.xlsx', index=False)
tabela_clientes_sp.to_excel(pasta_atual / 'planilhas_separadas' / 'SP.xlsx', index=False)

# Escrevendo todas consolidadas
with pd.ExcelWriter(pasta_atual / 'planilhas_consolidadas' / 'copia_clientes.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
    tabela_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index=False)
    tabela_clientes_pr.to_excel(nova_planilha, sheet_name='PR', index=False)
    tabela_clientes_sp.to_excel(nova_planilha, sheet_name='SP', index=False)
'''

tabela_clientes_dict = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name=None)

for nome_aba, tabela in tabela_clientes_dict.items():
    tabela.to_excel(pasta_atual / 'planilhas_separadas' / f'{nome_aba}.xlsx', index=False)


with pd.ExcelWriter(pasta_atual / 'planilhas_consolidadas' / 'clientes.xlsx') as consolidada:
    for arquivo in Path(pasta_atual / 'planilhas_separadas').glob('*.xlsx'):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada,sheet_name=arquivo.stem, index=False)


