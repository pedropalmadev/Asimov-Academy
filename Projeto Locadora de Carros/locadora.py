import os

def continuar_ou_sair():
    while True:
        opc2 = int(input("\033[32;1m[0]\033[m - Continuar | \033[31;1m[1]\033[m - Sair\n--> "))
        if opc2 == 0 or opc2 == 1:
            return opc2
        else:
            print("Digite um valor válido!")


def mostrar_carros():
    print()
    for indice, (nome_carro, valor) in portifolio.items():
        print(f"\033[36;1m[{indice}]\033[m {nome_carro} - R$ {valor} /dia")
    print()

def mostrar_carros_alugados():
    print()
    print("CARROS ALUGADOS\n")
    for i, [nome_carro,valor] in enumerate(carros_alugados):
        print(f"\033[36;1m[{i}]\033[m {nome_carro} - R$ {valor} /dia")
    print()


def atualizar_portfolio():
    global portifolio
    portifolio = {i: carro for i, carro in enumerate(portifolio.values())}


portifolio = {
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

while True:
    os.system("cls")
    print()
    print("="*30)
    print("\033[1m    LOCADORA DE CARROS!\033[m")
    print("=" * 30)
    print()
    opc = int(input(" - \033[1mOque deseja fazer?\033[0m\n\033[33;1m[0]\033[m - Mostrar portifólio | \033[33;1m[1]\033[m Alugar um carro | \033[33;1m[2]\033[m Devolver um carro\n--> "))
    if opc == 0:
        mostrar_carros()
        opc2 = continuar_ou_sair()
        if opc2 == 1:
            break
    elif opc == 1:
        mostrar_carros()
        while True:
            codcar = int(input("Escolha o código do carro\n--> "))
            if codcar in portifolio:
                diacar = int(input("Escolha quantos dias deseja alugar\n--> "))
                carro_escolhido = portifolio[codcar][0]
                os.system("cls")
                print(f"\nVocê escolheu \033[1m{portifolio[codcar][0]}\033[m por {diacar} dias.")
                aluguel = portifolio[codcar][1] * diacar
                print(f"O aluguel totalizaria \033[1mR$ {aluguel}\033[m. Deseja alugar?\n")
                sn = int(input("\033[32;1m[0]\033[m - Sim | \033[31;1m[1]\033[m - Não\n--> "))
                if sn == 0:
                    print(f"\nParabéns você alugou uma {carro_escolhido} por {diacar} dias.\n")
                    carros_alugados.append(portifolio.pop(codcar))
                    atualizar_portfolio()
                    break
                elif sn == 1:
                    print("\nOperação cancelada!\n")
                    break
                else:
                    print("\n\033[31;1mOpção inválido, tente novamente!\033[0m\n")
            else:
                print("\n\033[31;1mCódigo inválido, tente novamente!\033[0m\n")

        opc2 = continuar_ou_sair()
        if opc2 == 1:
            break

    elif opc == 2:
        while True:
            if not carros_alugados:
                print("\nNenhum carro para devolver\n")
                break
            else:
                mostrar_carros_alugados()
                codcar = int(input("Escolha o código do carro para devolver\n--> "))
                if 0 <= codcar < len(carros_alugados):
                    portifolio[len(portifolio)] = carros_alugados.pop(codcar)
                    atualizar_portfolio()
                    print("\nCarro devolvido com sucesso!\n")
                    break
                else:
                    print("\nCódigo inválido.\n")
        opc2 = continuar_ou_sair()
        if opc2 == 1:
            break
    else:
        print("Opção inválida. Tente novamente.")






