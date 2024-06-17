portfolio = {
    0: ["Chevrolet Tracker", 120],
    1: ["Chevrolet Onix", 90],
    2: ["Chevrolet Spin", 150],
    3: ["Hyundai HB20", 85],
    4: ["Hyundai Tucson", 120],
    5: ["Fiat Uno", 60],
    6: ["Fiat Mobi", 70],
    7: ["Fiat Pulse", 130]
}

carros_alugados = []


def mostrar_carros():
    for indice, (nome_carro, valor) in portfolio.items():
        print(f"{indice}: {nome_carro} = {valor}")


def continuar_ou_sair():
    while True:
        print("=" * 30)
        opc2 = int(input("[0] - Continuar | [1] - Sair\n--> "))
        if opc2 == 0 or opc2 == 1:
            return opc2
        else:
            print("Digite um valor válido!")


while True:
    print("=" * 30)
    print("Locadora de carros!")
    print("=" * 30)
    opc = int(input(
        " - O que deseja fazer?\n[0] - Mostrar portfólio | [1] - Alugar um carro | [2] - Devolver um carro\n--> "))

    if opc == 0:
        mostrar_carros()
        opc2 = continuar_ou_sair()
        if opc2 == 1:
            break

    elif opc == 1:
        mostrar_carros()
        while True:
            codcar = int(input("Escolha o código do carro\n--> "))
            if codcar in portfolio:
                diacar = int(input("Escolha quantos dias deseja alugar\n--> "))
                carro_escolhido = portfolio[codcar][0]
                print(f"Você escolheu {portfolio[codcar][0]} por {diacar} dias.")
                aluguel = portfolio[codcar][1] * diacar
                print(f"O aluguel totalizaria {aluguel}. Deseja alugar?")
                sn = int(input("[0] - Sim | [1] - Não\n--> "))
                if sn == 0:
                    print(f"\nParabéns, você alugou uma {carro_escolhido} por {diacar} dias.\n")
                    carros_alugados.append(portfolio.pop(codcar))
                    break
                elif sn == 1:
                    print("Operação cancelada.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Código de carro inválido. Tente novamente.")

        opc2 = continuar_ou_sair()
        if opc2 == 1:
            break

    else:
        print("Opção inválida. Tente novamente.")
