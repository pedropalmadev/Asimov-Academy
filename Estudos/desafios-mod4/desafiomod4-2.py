print('-=-'*20)
print('Início')
print('-=-'*20)
acertos = erros = tentativas = 0

estado_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal*': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
}

for n,e in estado_capitais.items():
    capital = input(f"\n --> Qual a capital do Estado {n}?: ")
    tentativas += 1
    if capital == e:
        print("Acertou!")
        acertos += 1
    else:
        print("Errou!")
        erros +=1
    while True:
        opt = input('\nDeseja continuar? [S/N]: ')
        if opt.lower() not in ['s','n']:
            print('Opção invalida')
        elif opt.lower() == 's':
            break
        else:
            break
    if opt.lower() == 'n':
        break
porc = acertos / tentativas * 100

print(f'Acertou {acertos} de {tentativas} rodadas')
print(f'Porcentagem de acertos: {porc:.2f}%')
