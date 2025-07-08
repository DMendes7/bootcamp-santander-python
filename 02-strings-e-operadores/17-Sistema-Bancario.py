menu = """
=======XuBank=======
1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair

Digite a opção desejada: """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if 0 < valor <= limite and numero_saques < LIMITE_SAQUES:
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido ou limite de saques atingido.")

    elif opcao == "3":
        print("\n===== Extrato =====")
        if extrato == "":
            print("Nenhuma transação realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("====================")

    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")