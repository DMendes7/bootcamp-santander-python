option = -1

while option != 0:
    option = int(input("Digite uma opção (0 para sair): "))
    if option == 1:
        print("Opção 1 selecionada")
    elif option == 2:
        print("Opção 2 selecionada")
    elif option == 3:
        print("Opção 3 selecionada")
    elif option == 4:
        break
    elif option == 0:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")