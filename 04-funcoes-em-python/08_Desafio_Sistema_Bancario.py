# Listas globais
usuarios = [
    {
        "nome": "João da Silva",
        "data_nascimento": "01-01-1990",
        "cpf": "12345678900",
        "endereco": "Rua A, 123 - Centro - São Paulo/SP"
    },
    {
        "nome": "Davi Oliveira",
        "data_nascimento": "05-08-1995",
        "cpf": "98765432100",
        "endereco": "Av B, 456 - Bairro X - Rio de Janeiro/RJ"
    }
]

contas = [
    {
        "agencia": "0001",
        "numero_conta": 1,
        "usuario": usuarios[0],
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    },
    {
        "agencia": "0001",
        "numero_conta": 2,
        "usuario": usuarios[1],
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
]

conta_ativa = None

# Funções
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf):
        print("Usuário já existente!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")


def login_conta():
    global conta_ativa
    cpf = input("Informe o CPF do titular da conta: ")
    numero = int(input("Informe o número da conta: "))

    for conta in contas:
        if conta["usuario"]["cpf"] == cpf and conta["numero_conta"] == numero:
            conta_ativa = conta
            print(f"Conta {numero} logada com sucesso.")
            return

    print("Conta não encontrada.")


def depositar():
    if conta_ativa is None:
        print("Nenhuma conta ativa. Use a opção 7 para acessar uma conta.")
        return

    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta_ativa["saldo"] += valor
        conta_ativa["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")


def sacar():
    if conta_ativa is None:
        print("Nenhuma conta ativa. Use a opção 7 para acessar uma conta.")
        return

    valor = float(input("Informe o valor do saque: "))
    limite = 500
    limite_saques = 3

    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > conta_ativa["saldo"]:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite de saque por operação.")
    elif conta_ativa["numero_saques"] >= limite_saques:
        print("Limite diário de saques atingido.")
    else:
        conta_ativa["saldo"] -= valor
        conta_ativa["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta_ativa["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")


def exibir_extrato():
    if conta_ativa is None:
        print("Nenhuma conta ativa. Use a opção 7 para acessar uma conta.")
        return

    print("\n===== Extrato =====")
    print(conta_ativa["extrato"] if conta_ativa["extrato"] else "Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {conta_ativa['saldo']:.2f}")
    print("====================")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {usuario['nome']}")


# Execução principal
def main():
    menu = """
======= XuBank =======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[7] Acessar conta
[0] Sair
=> """

    while True:
        opcao = input(menu)

        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            criar_usuario()
        elif opcao == "5":
            criar_conta()
        elif opcao == "6":
            listar_contas()
        elif opcao == "7":
            login_conta()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Início do programa
main()
